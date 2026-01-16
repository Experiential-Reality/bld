# TranslateX86ToRISCV

**Cost**: B + D×L = 49 + 1×0.432 = 49.432

---

## Structure

```
structure TranslateX86ToRISCV

B syscall_map: write | exit | read | open | close | mmap | munmap | brk
  write -> set(x86_num, 1), set(riscv_num, 64)
  exit -> set(x86_num, 60), set(riscv_num, 93)
  read -> set(x86_num, 0), set(riscv_num, 63)
  open -> set(x86_num, 2), set(riscv_num, 56)
  close -> set(x86_num, 3), set(riscv_num, 57)
  mmap -> set(x86_num, 9), set(riscv_num, 222)
  munmap -> set(x86_num, 11), set(riscv_num, 215)
  brk -> set(x86_num, 12), set(riscv_num, 214)
B reg_map_syscall: rax | rdi | rsi | rdx | r10 | r8 | r9
  rax -> set(riscv_reg, 17)
  rdi -> set(riscv_reg, 10)
  rsi -> set(riscv_reg, 11)
  rdx -> set(riscv_reg, 12)
  r10 -> set(riscv_reg, 13)
  r8 -> set(riscv_reg, 14)
  r9 -> set(riscv_reg, 15)
B reg_map_general: rax | rbx | rcx | rdx | rsp | rbp | rsi | rdi | r8 | r9 | r10 | r11 | r12 | r13 | r14 | r15
  rax -> set(riscv_reg, 10)
  rbx -> set(riscv_reg, 19)
  rcx -> set(riscv_reg, 12)
  rdx -> set(riscv_reg, 13)
  rsp -> set(riscv_reg, 2)
  rbp -> set(riscv_reg, 8)
  rsi -> set(riscv_reg, 11)
  rdi -> set(riscv_reg, 10)
  r8 -> set(riscv_reg, 14)
  r9 -> set(riscv_reg, 15)
  r10 -> set(riscv_reg, 16)
  r11 -> set(riscv_reg, 17)
  r12 -> set(riscv_reg, 20)
  r13 -> set(riscv_reg, 21)
  r14 -> set(riscv_reg, 22)
  r15 -> set(riscv_reg, 23)
B translate_op: mov_ri | mov_rr | add_rr | add_ri | sub_rr | sub_ri | xor_rr | and_rr | or_rr | cmp_rr | syscall | ret | nop | push | pop | jmp | je | jne
  mov_ri -> set(riscv_op, li), set(needs_reloc, 0)
  mov_rr -> set(riscv_op, mv)
  add_rr -> set(riscv_op, add)
  add_ri -> set(riscv_op, addi)
  sub_rr -> set(riscv_op, sub)
  sub_ri -> set(riscv_op, addi), set(negate_imm, 1)
  xor_rr -> set(riscv_op, xor)
  and_rr -> set(riscv_op, and)
  or_rr -> set(riscv_op, or)
  cmp_rr -> set(riscv_op, cmp_pending), set(cmp_left, $dst), set(cmp_right, $src)
  syscall -> set(riscv_op, ecall)
  ret -> set(riscv_op, ret)
  nop -> set(riscv_op, nop)
  push -> set(riscv_op, push_seq)
  pop -> set(riscv_op, pop_seq)
  jmp -> set(riscv_op, j)
  je -> set(riscv_op, beq)
  jne -> set(riscv_op, bne)

L parse_x86: binary_input -> x86_instructions (deps=0)
L map_instruction: x86_instruction -> riscv_instruction (deps=1)
L emit_riscv: riscv_instructions -> binary_output (deps=1)
L fixup_relocs: binary_output -> final_output (deps=1)

D instructions: N [input, sequential]
D riscv_instructions: M [output, sequential]

returns: final_output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| syscall_map | write \| exit \| read \| open \| close \| mmap \| munmap \| brk | topological |
| reg_map_syscall | rax \| rdi \| rsi \| rdx \| r10 \| r8 \| r9 | topological |
| reg_map_general | rax \| rbx \| rcx \| rdx \| rsp \| rbp \| rsi \| rdi \| r8 \| r9 \| r10 \| r11 \| r12 \| r13 \| r14 \| r15 | topological |
| translate_op | mov_ri \| mov_rr \| add_rr \| add_ri \| sub_rr \| sub_ri \| xor_rr \| and_rr \| or_rr \| cmp_rr \| syscall \| ret \| nop \| push \| pop \| jmp \| je \| jne | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| parse_x86 | binary_input | x86_instructions | 0 |  |
| map_instruction | x86_instruction | riscv_instruction | 1 |  |
| emit_riscv | riscv_instructions | binary_output | 1 |  |
| fixup_relocs | binary_output | final_output | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| instructions | N | input, sequential |
| riscv_instructions | M | output, sequential |

## Returns

`final_output`
