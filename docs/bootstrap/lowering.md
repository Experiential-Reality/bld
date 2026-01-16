# Lowering

**Cost**: B + D×L = 10 + 1×0.144 = 10.144

---

## Structure

```
structure Lowering

B operation: emit_byte | emit_u16 | emit_u32 | emit_u64 | syscall_write | syscall_exit | set_var | get_var | program_start | program_end
  emit_byte -> set(instruction, mov_ri), set(dst, rax), uses(X86)
  syscall_write -> set(mode_instruction, mov_ri), set(dst_lo, 0), set(dst_ext, 0), set(imm, 1), uses(X86), set(mode_instruction, mov_ri), set(dst_lo, 7), set(dst_ext, 0), set(imm, 1), uses(X86), set(mode_instruction, mov_ri), set(dst_lo, 6), set(dst_ext, 0), set(imm, $buffer), uses(X86), set(mode_instruction, mov_ri), set(dst_lo, 2), set(dst_ext, 0), set(imm, $length), uses(X86), set(mode_instruction, syscall), uses(X86)
  syscall_exit -> set(mode_instruction, mov_ri), set(dst_lo, 0), set(dst_ext, 0), set(imm, 60), uses(X86), set(mode_instruction, mov_ri), set(dst_lo, 7), set(dst_ext, 0), set(imm, $exit_code), uses(X86), set(mode_instruction, syscall), uses(X86)
  program_start -> set(mode_instruction, prologue), uses(X86)
  program_end -> set(mode_instruction, epilogue), uses(X86)

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
