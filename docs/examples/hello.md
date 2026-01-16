# Hello

**Cost**: B + D×L = 3 + 1×0.144 = 3.144

---

## Structure

```
structure Hello

B code: write_syscall | exit_syscall | string_data
  write_syscall -> emit_byte(0x48), emit_byte(0xC7), emit_byte(0xC0), emit_byte(0x01), emit_byte(0x00), emit_byte(0x00), emit_byte(0x00), emit_byte(0x48), emit_byte(0xC7), emit_byte(0xC7), emit_byte(0x01), emit_byte(0x00), emit_byte(0x00), emit_byte(0x00), emit_byte(0x48), emit_byte(0x8D), emit_byte(0x35), emit_byte(0x19), emit_byte(0x00), emit_byte(0x00), emit_byte(0x00), emit_byte(0x48), emit_byte(0xC7), emit_byte(0xC2), emit_byte(0x0C), emit_byte(0x00), emit_byte(0x00), emit_byte(0x00), emit_byte(0x0F), emit_byte(0x05)
  exit_syscall -> emit_byte(0x48), emit_byte(0xC7), emit_byte(0xC0), emit_byte(0x3C), emit_byte(0x00), emit_byte(0x00), emit_byte(0x00), emit_byte(0x48), emit_byte(0xC7), emit_byte(0xC7), emit_byte(0x00), emit_byte(0x00), emit_byte(0x00), emit_byte(0x00), emit_byte(0x0F), emit_byte(0x05)
  string_data -> emit_byte(0x48), emit_byte(0x65), emit_byte(0x6C), emit_byte(0x6C), emit_byte(0x6F), emit_byte(0x2C), emit_byte(0x20), emit_byte(0x42), emit_byte(0x4C), emit_byte(0x44), emit_byte(0x21), emit_byte(0x0A)

L emit: code -> output (deps=1)

D output: N [output, sequential]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| code | write_syscall \| exit_syscall \| string_data | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| emit | code | output | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| output | N | output, sequential |

## Returns

`output`
