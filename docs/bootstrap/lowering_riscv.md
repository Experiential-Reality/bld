# LoweringRISCV

**Cost**: B + D×L = 10 + 1×0.144 = 10.144

---

## Structure

```
structure LoweringRISCV

B operation: emit_byte | emit_u16 | emit_u32 | emit_u64 | syscall_write | syscall_exit | set_var | get_var | program_start | program_end
  emit_byte -> set(mode_instruction, li), set(rd, 10), set(imm, $byte), uses(RISCV)
  emit_u16 -> set(mode_instruction, li), set(rd, 10), set(imm, $value), uses(RISCV)
  emit_u32 -> set(mode_instruction, li), set(rd, 10), set(imm, $value), uses(RISCV)
  emit_u64 -> set(mode_instruction, li), set(rd, 10), set(imm, $value), uses(RISCV)
  syscall_write -> set(mode_instruction, li), set(rd, 17), set(imm, 64), uses(RISCV), set(mode_instruction, li), set(rd, 10), set(imm, 1), uses(RISCV), set(mode_instruction, li), set(rd, 11), set(imm, $buffer), uses(RISCV), set(mode_instruction, li), set(rd, 12), set(imm, $length), uses(RISCV), set(mode_instruction, ecall), uses(RISCV)
  syscall_exit -> set(mode_instruction, li), set(rd, 17), set(imm, 93), uses(RISCV), set(mode_instruction, li), set(rd, 10), set(imm, $exit_code), uses(RISCV), set(mode_instruction, ecall), uses(RISCV)
  set_var -> set(mode_instruction, li), set(rd, $reg), set(imm, $value), uses(RISCV)
  get_var -> set(mode_instruction, mv), set(rd, $dst), set(rs1, $src), uses(RISCV)
  program_start -> set(mode_instruction, prologue), uses(RISCV)
  program_end -> set(mode_instruction, epilogue), uses(RISCV)

L lower_all: operations -> instructions (deps=1)
L lower_one: operation -> instruction_seq (deps=0)

D operations: N [input, from_structure]
D instructions: M [output, sequential]

returns: instructions
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| operation | emit_byte \| emit_u16 \| emit_u32 \| emit_u64 \| syscall_write \| syscall_exit \| set_var \| get_var \| program_start \| program_end | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| lower_all | operations | instructions | 1 |  |
| lower_one | operation | instruction_seq | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| operations | N | input, from_structure |
| instructions | M | output, sequential |

## Returns

`instructions`
