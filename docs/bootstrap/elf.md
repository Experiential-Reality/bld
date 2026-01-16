# ELF64

**Cost**: B + D×L = 12 + 1×0.432 = 12.432

---

## Structure

```
structure ELF64

B emit: full | header_only | phdr_only
  full -> emit_bytes(0x7F, 0x45, 0x4C, 0x46), emit_byte(0x02), emit_byte(0x01), emit_byte(0x01), emit_byte(0x00), emit_bytes(0, 0, 0, 0, 0, 0, 0, 0), emit_u16(0x02), emit_u16(0x3E), emit_u32(0x01), emit_u64($entry), emit_u64(0x40), emit_u64(0x00), emit_u32(0x00), emit_u16(0x40), emit_u16(0x38), emit_u16(0x01), emit_u16(0x40), emit_u16(0x00), emit_u16(0x00), emit_u32(0x01), emit_u32(0x05), emit_u64(0x00), emit_u64($base), emit_u64($base), emit_u64($filesz), emit_u64($filesz), emit_u64(0x1000), emit($code)
  header_only -> emit_bytes(0x7F, 0x45, 0x4C, 0x46), emit_byte(0x02), emit_byte(0x01), emit_byte(0x01), emit_byte(0x00), emit_bytes(0, 0, 0, 0, 0, 0, 0, 0), emit_u16(0x02), emit_u16(0x3E), emit_u32(0x01), emit_u64($entry), emit_u64(0x40), emit_u64(0x00), emit_u32(0x00), emit_u16(0x40), emit_u16(0x38), emit_u16(0x01), emit_u16(0x40), emit_u16(0x00), emit_u16(0x00)
  phdr_only -> emit_u32(0x01), emit_u32(0x05), emit_u64(0x00), emit_u64($base), emit_u64($base), emit_u64($filesz), emit_u64($filesz), emit_u64(0x1000)
B elf_header: magic | class | data | version | osabi | type | machine
  magic -> emit_bytes(0x7F, 0x45, 0x4C, 0x46)
  class -> emit_byte(0x02)
  data -> emit_byte(0x01)
  version -> emit_byte(0x01)
  osabi -> emit_byte(0x00)
  type -> emit_u16(0x02)
  machine -> emit_u16(0x3E)
B phdr: p_type | p_flags
  p_type -> emit_u32(0x01)
  p_flags -> emit_u32(0x05)

L emit_elf_header: unit -> output (deps=1)
L emit_phdr: code -> output (deps=1)
L emit_code: code -> output (deps=0)
L emit_elf: code -> output (deps=1)

D code: N [input, sequential]
D output: M [output, sequential]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| emit | full \| header_only \| phdr_only | topological |
| elf_header | magic \| class \| data \| version \| osabi \| type \| machine | topological |
| phdr | p_type \| p_flags | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| emit_elf_header | unit | output | 1 |  |
| emit_phdr | code | output | 1 |  |
| emit_code | code | output | 0 |  |
| emit_elf | code | output | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| code | N | input, sequential |
| output | M | output, sequential |

## Returns

`output`
