// SPDX-LICENSE-IDENTIFIER: GPL
#include <asm/asm-uaccess.h>
#include <asm/assembler.h>

.arch armv8-a
// .extern kernel_space_arr

.section ".modinfo", "ax"
.global __this_module_license 
__this_module_license: 
	.asciz "license=GPL"

.section ".real_hooker", "ax"
SYM_FUNC_START(real_hooker)
	// something went wrong but we can not distinguish it now...
	// maybe cocurrency cause crash, which seems to be inevitable and extremely hard to bypass or to protect...
	stp		x2, x3, [x1]
	stp		x4, x5, [x1, #16]
	stp		x6, x7, [x1, #32]
	stp		x8, x9, [x1, #48]
	stp		x10, x11, [x1, #64]
	stp		x12, x13, [x1, #80]
	stp		x14, x15, [x1, #96]
	stp		x16, x17, [x1, #112]
	stp		x18, x19, [x1, #128]
	stp		x20, x21, [x1, #144]
	stp		x22, x23, [x1, #160]
	stp		x24, x25, [x1, #176]
	stp		x26, x27, [x1, #192]
	stp		x28, x29, [x1, #208]
	str		x30, [x1, #224]	

	mrs		x0, VBAR_EL1
	sub		x0, x0, #0x5D0
	ldp		x0, x1, [x0]		// 0xa30 pwned_string, 0xa38 record_func 
	blr		x1
	mrs		x0, VBAR_EL1
	sub		x0, x0, #0x5E0		// 0xa20 real_hooker, 0xa28 kernel_space_arr 
	ldp		x0, x1, [x0]

	ldr		x30, [x1, #224]
	ldp		x28, x29, [x1, #208]
	ldp		x26, x27, [x1, #192]
	ldp		x24, x25, [x1, #176]
	ldp		x22, x23, [x1, #160]
	ldp		x20, x21, [x1, #144]
	ldp		x18, x19, [x1, #128]
	ldp		x16, x17, [x1, #112]
	ldp		x14, x15, [x1, #96]
	ldp		x12, x13, [x1, #80]
	ldp		x10, x11, [x1, #64]
	ldp		x8, x9, [x1, #48]
	ldp		x6, x7, [x1, #32]
	ldp		x4, x5, [x1, #16]
	ldp		x2, x3, [x1]
	ret
SYM_FUNC_END(real_hooker)

.section .rodata
.global PWNED_STRING
PWNED_STRING:
    .asciz "\0016\033[1;36mHello world from corrupted exception vectors table.\033[0m\n"
.align 4

.section .text
.global	exception_vector_hooker
exception_vector_hooker:
	// location-independent assembly code.
	stp x0, x29, [sp, #-0x18]
	stp x1, x30, [sp, #-0x28]
	mrs x0, VBAR_EL1
	sub x0, x0, #0x5E0
	ldp x0, x1, [x0]		// 0xa20 x0, 0xa28, x1
	blr x0					// real_hooker, kernel_space
	ldp x0, x29, [sp, #-0x18]
	ldp x1, x30, [sp, #-0x28]
.align 3

//! DRAFT ZONE...
/* 

*/



//! ABORT CODE ZONE
/*

*/

