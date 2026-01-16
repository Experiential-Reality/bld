# LoweringAArch64

**Cost**: B + D×L = 10 + 1×0.144 = 10.144

---

## Structure

```
structure LoweringAArch64

B operation: emit_byte | emit_u16 | emit_u32 | emit_u64 | syscall_write | syscall_exit | set_var | get_var | program_start | program_end
  emit_byte -> set(mode_instruction, mov_ri), set(rd, 0), set(imm, $byte), uses(AArch64)
  emit_u16 -> set(mode_instruction, mov_ri), set(rd, 0), set(imm, $value), uses(AArch64)
  emit_u32 -> set(mode_instruction, mov_ri), set(rd, 0), set(imm, $value), uses(AArch64)
  emit_u64 -> set(mode_instruction, mov_ri), set(rd, 0), set(imm, $value), uses(AArch64)
  syscall_write -> set(mode_instruction, mov_ri), set(rd, 8), set(imm, 64), uses(AArch64), set(mode_instruction, mov_ri), set(rd, 0), set(imm, 1), uses(AArch64), set(mode_instruction, mov_ri), set(rd, 1), set(imm, $buffer), uses(AArch64), set(mode_instruction, mov_ri), set(rd, 2), set(imm, $length), uses(AArch64), set(mode_instruction, svc), set(imm, 0), uses(AArch64)
  syscall_exit -> set(mode_instruction, mov_ri), set(rd, 8), set(imm, 93), uses(AArch64), set(mode_instruction, mov_ri), set(rd, 0), set(imm, $exit_code), uses(AArch64), set(mode_instruction, svc), set(imm, 0), uses(AArch64)
  set_var -> set(mode_instruction, mov_ri), set(rd, $reg), set(imm, $value), uses(AArch64)
  get_var -> set(mode_instruction, mov_rr), set(rd, $dst), set(rm, $src), uses(AArch64)
  program_start -> set(mode_instruction, prologue), uses(AArch64)
  program_end -> set(mode_instruction, epilogue), uses(AArch64)

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
