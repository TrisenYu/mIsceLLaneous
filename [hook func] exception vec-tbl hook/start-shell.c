// SPDX-LICENSE-IDENTIFIER: GPL
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/init.h>
#include <linux/mm.h>
#include <linux/io.h>
#include <linux/iomap.h>
#include <linux/slab.h>

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Exception Vector Overlapping and Hooking execution flow test.");
MODULE_AUTHOR("kisfg@hotmail.com");

typedef enum _choice { DISABLE, ENABLE } Choice;
char kernel_space_arr[1024] = {0}, msg_arr[512] = {0};
size_t msg_ptr, interrupt_cnt;

extern void real_hooker(void);
extern const char *PWNED_STRING;				// 汇编引入
extern void exception_vector_hooker(void);			// 汇编实现此函数


/*
 * @param exec_inst 待执行指令 32 bits 十六进制值 传入形式：指针。
 * @param origin_pc 待执行指令原先所处地址
 * @param target_pc 待执行指令将迁移地址
 * @details 有此函数后，可实现任意函数跳转并返回。不需要再额外使用过于复杂的重定位
 * 
 * note: 偏移量超出 +/- 4GB 时不可行。
*/
static size_t bl_relocation_func(unsigned int *exec_inst, size_t origin_pc, size_t target_pc)
{
    /* 
	   BL instruction.

        31   26|25  0|
		1001_01|imm26|
		0x9  
    */
    const size_t branch_mask = 0x03FFFFFF, 
                 branch_addr_erase = 0xFC000000,
                 sign_flip_mask = 0xFFFFFFFFFC000000;

	printk("old pc, target pc = 0x%016lx, 0x%016lX\n", origin_pc, target_pc);

    size_t abs_shift = max(origin_pc, target_pc) - min(origin_pc, target_pc);

	long long shift_direction = abs_shift;
	if (target_pc == max(origin_pc, target_pc))
		shift_direction = -(long long)(abs_shift);	

    long long inst_addr_ofs = (*exec_inst & branch_mask) * 4 /* sizeof instruction */;
	if (inst_addr_ofs & 0x80000000)
		inst_addr_ofs |= sign_flip_mask;
    
    /* 
	   pc + inst_addr_ofs = inst_addr
       target_pc + direction --> pc
	   target_pc + shift_direction + inst_addr_ofs = inst_addr.
    */ 
    long long res_ofs = (inst_addr_ofs + shift_direction) >> 2;

    printk("res-ofs = 0x%016llX\n", (unsigned long long)res_ofs);
    if ((res_ofs & sign_flip_mask) != sign_flip_mask) {
        printk("Can't revise the branch address.\n");
        return ~0;
    }
    res_ofs &= branch_mask;
    *exec_inst &= branch_addr_erase,
    *exec_inst |= res_ofs;
    return res_ofs;
}


unsigned long long ttbr1;
#define		ADDRBIT(x)		((size_t)x & 0x0000FFFFFFFFFFFEull)
#define		DESCRIPTOR(x)	((size_t)x & 0x0000FFFFFFFFF000ull)

/*  https://hjk.life/posts/linux-kernel-interrupt/
 *  5|5|                     1|1|0  0|0  0|0|0  0
 *  4|3|                     1|0|9  8|7  6|5|4  2
 * +-+-+--------------------+-+-+----+----+-+----+--+
 * |U|P|effective           |n|A|SHar|Acce|N|MAIR|  |
 * |X|X|     *   *   *      | | |e   |ss  | |    |  |
 * |N|N|       physical addr|G|F|attr|Perm|S|indx|  |
 * +-+-+--------------------+-+-+----+----+-+----+--+
 63 - 59 是否存在后门？
    用户级AP     特权级 AP
    不可访问      读写					00 xx xxxx
    访问          读写					01 xx xxxx
    不可访问      只读					10 xx xxxx
    访问          只读(?unread)		    11 xx xxxx
                    |
                    +--> 测试以后感觉不可读。
*/
static void pgtable_walk_and_set_rwable(size_t kvaddr, Choice choice)
{
    size_t enable_rw = 0xFFFFFFFFFFFFFF7FULL,
           enable_ro = 0x00000000000000B0ULL,
           lv0ofs = ((kvaddr >> 39) & 0x1FF) << 3,
           lv1ofs = ((kvaddr >> 30) & 0x1FF) << 3,
           lv2ofs = ((kvaddr >> 21) & 0x1FF) << 3,
           lv3ofs = ((kvaddr >> 12) & 0x1FF) << 3,

           pselv0 = ADDRBIT(ttbr1) + lv0ofs,
           vselv0 = (size_t)__va((void *)pselv0),

           pslv1b = *(size_t *)vselv0,
           pselv1 = DESCRIPTOR(pslv1b) + lv1ofs,
           vselv1 = (size_t)__va((void *)pselv1),

           pslv2b = *(size_t *)vselv1,
           pselv2 = DESCRIPTOR(pslv2b) + lv2ofs,
           vselv2 = (size_t)__va((void *)pselv2),

           pslv3b = *(size_t *)vselv2,
           pselv3 = DESCRIPTOR(pslv3b) + lv3ofs,
           vselv3 = (size_t)__va((void *)pselv3);
    /* modify the memory attribute of the final page. */
    if (choice) *(unsigned long long *)vselv3 &= enable_rw;
    else *(unsigned long long *)vselv3 |= enable_ro;
}
#undef ADDRBIT
#undef DESCRIPTOR

unsigned long long vectorbase;
//! el1t handler  UNHANDLED
#define 	sp0sync		vectorbase + 0x000
#define 	sp0irq 		vectorbase + 0x080
#define 	sp0fiq 		vectorbase + 0x100
#define 	sp0ser 		vectorbase + 0x180
//! el1h handler
#define 	spxsync		vectorbase + 0x200 		/* el1h_sync_handler 0xffffb959f5877a3c */
#define 	spxirq 		vectorbase + 0x280
#define 	spxfiq 		vectorbase + 0x300
#define 	spxser 		vectorbase + 0x380
//! el0 64 handler
#define 	A64sync		vectorbase + 0x400
#define 	A64irq 		vectorbase + 0x480
#define 	A64fiq 		vectorbase + 0x500
#define 	A64ser 		vectorbase + 0x580
//! el0 32 handler UNHANDLED
#define 	A32sync 	vectorbase + 0x600
#define 	AA32irq 	vectorbase + 0x680
#define 	AA32fiq 	vectorbase + 0x700
#define 	AA32ser 	vectorbase + 0x780

unsigned int shellcode_arr[128] = {0};
size_t shellcode_cnt = 0, recover_ptr = 8;
static inline void access_original_asm(size_t kvaddr)
{
    for (size_t _ = 0; _ < 32; _++, shellcode_cnt++)
        shellcode_arr[shellcode_cnt] = *(unsigned int *)(kvaddr + (_ << 2));
}

static inline void read_shellcode(size_t kvaddr)
{
    for (; shellcode_cnt < recover_ptr; shellcode_cnt++)
        shellcode_arr[shellcode_cnt] = *(unsigned int *)(kvaddr + (shellcode_cnt << 2));
}

static void read_sysregister(void)
{
    asm volatile("mrs x0, TTBR1_EL1\n\t"
                 "str x0, %[ttbr1_base]\n\t"
                 "mrs x0, VBAR_EL1\n\t"
                 "str x0, %[vbar]"
                 : [ttbr1_base] "=m"(ttbr1), [vbar] "=m"(vectorbase)
                 :
                 : "memory");
}
static void modify_exception_vectors(size_t tvaddr, size_t recover)
{
    for (size_t _ = 0; _ < 32; _++)
        *(unsigned int *)(tvaddr + (_ << 2)) = shellcode_arr[_ + recover];
}

void record_func(const char* string)
{
	// todo: concurrency might corrupt the execution logic, which seems to be unsolvable?
	if (!!msg_ptr) { 
		interrupt_cnt ++; 
		return; 
	}
	for (msg_ptr = 0; string[msg_ptr] != '\0'; msg_ptr ++)
		msg_arr[msg_ptr] = string[msg_ptr];
}
size_t selector;
static int __init load_shellcode(void)
{
    read_sysregister();
    pgtable_walk_and_set_rwable(vectorbase, ENABLE);
    pgtable_walk_and_set_rwable(vectorbase - 0x1000, ENABLE);

	selector = (vectorbase - 0x1000 + 0xa00);
	printk("<check>: rh, ks, pw, rf = 0x%016llX, 0x%016llX, 0x%016llX, 0x%016llX\n",
			(unsigned long long)real_hooker,   (unsigned long long)kernel_space_arr,
			(unsigned long long)&PWNED_STRING, (unsigned long long)record_func);

	/* assembly code needed. */
	*(unsigned long long*)(selector + 4 * 8) = (unsigned long long)real_hooker,
	*(unsigned long long*)(selector + 5 * 8) = (unsigned long long)kernel_space_arr,
	*(unsigned long long*)(selector + 6 * 8) = (unsigned long long)&PWNED_STRING,
	*(unsigned long long*)(selector + 7 * 8) = (unsigned long long)record_func;

	printk("module-vaddr = 0x%016llX\nvbar = 0x%016llX, jmp-addr = 0x%016llX\n", 
			(unsigned long long)load_shellcode,(unsigned long long)vectorbase, 
			(unsigned long long)exception_vector_hooker);
	
    read_shellcode((size_t)exception_vector_hooker); // 先读原始内容再去写。
	/*
    	bl_relocation_func(&shellcode_arr[recover_ptr - 1], 
    	                   (size_t)(exception_vector_hooker) + 0xC, 
    	                   spxirq + 0xC);
	*/

    access_original_asm(spxfiq);
    modify_exception_vectors(spxfiq, 0);

	/* output-and-test */
	printk("addr-interrupt-cnt = 0x%016llX\n", (unsigned long long)&interrupt_cnt);
	for (size_t _ = 0; _ < 16; _ ++)
		printk("interrupt-cnt = 0x%016lX\n", interrupt_cnt);

    printk("msg<%ld>\n\t", msg_ptr); 
	if (!!msg_ptr) printk(msg_arr);

	/* just for test. */
	for (size_t _ = 0; _ < 10; _ ++)
		if (!!msg_ptr) printk(msg_arr);
    return 0;
}

static void __exit exit_shellcode(void)
{
    /* recover test. */
    modify_exception_vectors(spxfiq, recover_ptr);
    pgtable_walk_and_set_rwable(vectorbase, DISABLE);
	for (size_t _ = 4; _ < 8; _ ++)
		*(unsigned long long*)(selector + _ * 8) = 0; 
	printk("total-interrupt-cnt = 0x%016lX\n", interrupt_cnt);
    pgtable_walk_and_set_rwable(vectorbase - 0x1000, DISABLE);
}

module_init(load_shellcode);
module_exit(exit_shellcode);
