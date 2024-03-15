#! /usr/bin/python3
# -*- coding: utf-8 -*-
# SPDX-LICENSE-IDENTIFIER: GPL
# AUTHOR: also123sao@163.com
""" 针对 windows 下的串口字节传输装置。 """
import serial.tools.list_ports
import win32api, win32con, win32gui, os
from ctypes import *
from ctypes import wintypes as w

UnsignedLong_PTR = c_ulong if sizeof(c_void_p) == 4 else c_ulonglong


class KeyBoard_Input(Structure):
    _fields_ = [('wVk', w.WORD),
                ('wScan', w.WORD),
                ('dwFlags', w.DWORD),
                ('time', w.DWORD),
                ('dwExtraInfo', UnsignedLong_PTR)]


class Mouse_Input(Structure):
    _fields_ = [('dx', w.LONG),
                ('dy', w.LONG),
                ('mouseData', w.DWORD),
                ('dwFlags', w.DWORD),
                ('time', w.DWORD),
                ('dwExtraInfo', UnsignedLong_PTR)]


class Hardware_Input(Structure):
    _fields_ = [('uMsg', w.DWORD),
                ('wParamL', w.WORD),
                ('wParamH', w.WORD)]


class Binding_Input(Union):
    _fields_ = [('mi', Mouse_Input),
                ('ki', KeyBoard_Input),
                ('hi', Hardware_Input)]


class KMH_Input(Structure):
    _anonymous_ = ['u']                     # c 中的 union 类型
    _fields_ = [('type', w.DWORD),
                ('u', Binding_Input)]


lib = WinDLL('user32')
lib.SendInput.argtypes = w.UINT, POINTER(KMH_Input), c_int
lib.SendInput.restype = w.UINT


def Analog_PressKey(_data: int) -> None:
    # 此处相当于向上位机发送硬件编码
    _Input = KMH_Input()
    _Shift = KMH_Input()

    _Shift.type = _Input.type = 1       # 代表 INPUT_KEYBOARD 类型

    _Input.ki = KeyBoard_Input(_data, _data, 0, 0, 0)
    _Shift.ki = KeyBoard_Input(0x10, 0x10, 0, 0, 0)

    if 0x61 <= _data <= 0x7a:           # 97-122 大写改发小写
        _Input.ki.wVk = _Input.ki.wScan - 0x20
        _Input.ki.wScan = _Input.ki.wVk
    elif 0x41 <= _data <= 0x5a:         # 65-90
        lib.SendInput(1, byref(_Shift), sizeof(KMH_Input))
        _Shift.ki.dwFlags |= 0x2

    lib.SendInput(1, byref(_Input), sizeof(KMH_Input))
    _Input.ki.dwFlags |= 0x2            # 代表抬起手指
    lib.SendInput(1, byref(_Input), sizeof(KMH_Input))

    if 0x41 <= _data <= 0x5a:
        lib.SendInput(1, byref(_Shift), sizeof(KMH_Input))


def read_send_from_serial():
    """
        # 注意 WM_IME_CHAR 和 WM_CHAR 的区别
        # 致谢： https://blog.csdn.net/zhuisui_woxin/article/details/84256343
    """
    global ser
    lst = -1
    while True:
        point = win32api.GetCursorPos()                 # 获取鼠标所在的位置
        hwnd = win32gui.WindowFromPoint(point)          # 通过鼠标来找到主窗口句柄
        process_title = win32gui.GetWindowText(hwnd)    # 主窗口名称
        try:
            com_input = ser.read()
            if com_input:
                if lst != hwnd:
                    lst = hwnd
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, point[0], point[1], 0, 0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, point[0], point[1], 0, 0)

                print(f'> 即将发送 {com_input} 到 ({point[0]}, {point[1]})'
                      f'\t--->\t[{hwnd}]:{process_title}')
                _num = com_input[0].from_bytes(byteorder='little', bytes=com_input)

                if 48 <= _num <= 57 or 65 <= _num <= 90 or 97 <= _num <= 122:
                    Analog_PressKey(_num)
                else:
                    win32gui.PostMessage(hwnd, win32con.WM_IME_CHAR, com_input[0], 0) # 用 SendMessage 也一样。
        except BaseException as e:
            print("> 进程收到中断命令。" if isinstance(e, KeyboardInterrupt) else f"> 如突然拔出单片机等未定义异常({e})！")
            exit(0)


def send_2_serial_and_set():
    global ser
    while True:
        try:
            repeat_times, a_byte = map(int,
                                       input("> 十进制表示下，输入重复次数以及目的字节并以空格隔开。"
                                             "重复次数为 0 的将停止发送。\n> ").split(' '))
            if repeat_times > 0xFF or repeat_times < 0 or a_byte > 0xFF or a_byte < 0:
                print("> 必须是一个字节内的无符号数。")
                continue
            elif repeat_times == 0:
                break
            data = bytearray([0xFF, 0xEE, repeat_times, a_byte])
            if ser.writable():
                ser.write(data)
        except ValueError:
            continue
        except KeyboardInterrupt:
            # 直接停止就好
            print("> 接收到中断请求。")
            break
        except BaseException as e:
            print(f"> 如突然拔出单片机等未定义异常({e})！")
            exit(0)


if __name__ == '__main__':
    print('\n> [OS-Name]:', os.name,
          '\n> 这是一个在 windows 环境下可转发或设置串口数据的简易程序。')

    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        print("> 无串口设备。")
        exit(0)

    print("> 可用的串口设备如下：")
    for comport in ports_list:
        print(list(comport)[0], list(comport)[1])

    print("> 默认取第一个为单片机。")
    ser = serial.Serial(f"{ports_list[0][0]}", 9600,    # 指定串口与通信波特率
                        bytesize=serial.EIGHTBITS,      # 数据位 8
                        parity=serial.PARITY_NONE,      # 无校验位
                        stopbits=serial.STOPBITS_ONE,   # 停止位 1
                        timeout=1)                      # 超时时间 1 s
    if not ser.isOpen():
        print("> 打开串口失败。")
        exit(0)

    print(f"> 打开串口成功。\n{ser.name}")
    while True:
        try:
            mode_switch = input('> 选择此进程的运行模式。\n\t'
                                '1. 读取字节（不可返回父级）；\n\t'
                                '2. 设置字节；\n\t'
                                '3. 退出.\n> ')
        except UnicodeDecodeError or KeyboardInterrupt:
            break

        try:
            mode = int(mode_switch)
        except ValueError:
            print("> 选择有误。")
            continue
        except KeyboardInterrupt or UnicodeDecodeError:
            break

        if mode == 1:
            read_send_from_serial()
        elif mode == 2:
            send_2_serial_and_set()
        elif mode == 3:
            break

    ser.close()
    print("[程序终止运行。]")
