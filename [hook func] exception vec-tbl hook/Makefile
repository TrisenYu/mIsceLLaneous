SHELL := /bin/zsh

MODULE_NAME = shellcode

ifneq  ($(KERNELRELEASE),)
	obj-m := shellcode.o
	shellcode-objs := start-shell.o jmp.o
else
    KERNEL_DIR = /media/cdrom/LinuxSourceCode/linux-6.6.6
    PATH_NOW = $(shell pwd)/

all:
	make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- -C $(KERNEL_DIR)  M=$(PATH_NOW) modules
clean:
	rm -f *.ko *.o *.mod* *.symvers *.order .*.cmd
endif
