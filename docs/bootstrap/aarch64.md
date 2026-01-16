# AArch64

**Cost**: B + D×L = 93 + 1×0.288 = 93.288

---

## Structure

```
structure AArch64

B instruction: add_rr | add_ri | sub_rr | sub_ri | adds_rr | subs_rr | and_rr | and_ri | orr_rr | orr_ri | eor_rr | eor_ri | mov_rr | mov_ri | movz | movk | movn | ldr | ldrb | ldrh | ldrsw | ldrsb | ldrsh | str | strb | strh | ldp | stp | b | bl | br | blr | ret | cbz | cbnz | tbz | tbnz | cmp_rr | cmp_ri | tst_rr | beq | bne | blt | bgt | ble | bge | blo | bhi | bls | bhs | svc | nop | prologue | epilogue
  add_rr -> emit_u32(0x8B000000 | ($rm << 16) | ($rn << 5) | $rd)
  add_ri -> emit_u32(0x91000000 | (($imm & 0xFFF) << 10) | ($rn << 5) | $rd)
  sub_rr -> emit_u32(0xCB000000 | ($rm << 16) | ($rn << 5) | $rd)
  sub_ri -> emit_u32(0xD1000000 | (($imm & 0xFFF) << 10) | ($rn << 5) | $rd)
  adds_rr -> emit_u32(0xAB000000 | ($rm << 16) | ($rn << 5) | $rd)
  subs_rr -> emit_u32(0xEB000000 | ($rm << 16) | ($rn << 5) | $rd)
  and_rr -> emit_u32(0x8A000000 | ($rm << 16) | ($rn << 5) | $rd)
  and_ri -> emit_u32(0x92400000 | ($rn << 5) | $rd | (($imm & 0x3F) << 10))
  orr_rr -> emit_u32(0xAA000000 | ($rm << 16) | ($rn << 5) | $rd)
  orr_ri -> emit_u32(0xB2400000 | ($rn << 5) | $rd | (($imm & 0x3F) << 10))
  eor_rr -> emit_u32(0xCA000000 | ($rm << 16) | ($rn << 5) | $rd)
  eor_ri -> emit_u32(0xD2400000 | ($rn << 5) | $rd | (($imm & 0x3F) << 10))
  mov_rr -> emit_u32(0xAA0003E0 | ($rm << 16) | $rd)
  mov_ri -> emit_u32(0xD2800000 | (($imm & 0xFFFF) << 5) | $rd)
  movz -> emit_u32(0xD2800000 | (($shift & 0x30) << 17) | (($imm & 0xFFFF) << 5) | $rd)
  movk -> emit_u32(0xF2800000 | (($shift & 0x30) << 17) | (($imm & 0xFFFF) << 5) | $rd)
  movn -> emit_u32(0x92800000 | (($shift & 0x30) << 17) | (($imm & 0xFFFF) << 5) | $rd)
  ldr -> emit_u32(0xF9400000 | ((($offset >> 3) & 0xFFF) << 10) | ($rn << 5) | $rt)
  ldrb -> emit_u32(0x39400000 | (($offset & 0xFFF) << 10) | ($rn << 5) | $rt)
  ldrh -> emit_u32(0x79400000 | ((($offset >> 1) & 0xFFF) << 10) | ($rn << 5) | $rt)
  ldrsw -> emit_u32(0xB9800000 | ((($offset >> 2) & 0xFFF) << 10) | ($rn << 5) | $rt)
  ldrsb -> emit_u32(0x39800000 | (($offset & 0xFFF) << 10) | ($rn << 5) | $rt)
  ldrsh -> emit_u32(0x79800000 | ((($offset >> 1) & 0xFFF) << 10) | ($rn << 5) | $rt)
  str -> emit_u32(0xF9000000 | ((($offset >> 3) & 0xFFF) << 10) | ($rn << 5) | $rt)
  strb -> emit_u32(0x39000000 | (($offset & 0xFFF) << 10) | ($rn << 5) | $rt)
  strh -> emit_u32(0x79000000 | ((($offset >> 1) & 0xFFF) << 10) | ($rn << 5) | $rt)
  ldp -> emit_u32(0xA9400000 | (((($offset >> 3) & 0x7F) << 15)) | ($rt2 << 10) | ($rn << 5) | $rt)
  stp -> emit_u32(0xA9000000 | (((($offset >> 3) & 0x7F) << 15)) | ($rt2 << 10) | ($rn << 5) | $rt)
  b -> emit_u32(0x14000000 | ((($offset >> 2) & 0x3FFFFFF)))
  bl -> emit_u32(0x94000000 | ((($offset >> 2) & 0x3FFFFFF)))
  br -> emit_u32(0xD61F0000 | ($rn << 5))
  blr -> emit_u32(0xD63F0000 | ($rn << 5))
  ret -> emit_u32(0xD65F03C0)
  cbz -> emit_u32(0xB4000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | $rt)
  cbnz -> emit_u32(0xB5000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | $rt)
  tbz -> emit_u32(0x36000000 | ((($bit >> 5) & 0x1) << 31) | (($bit & 0x1F) << 19) | (((($offset >> 2) & 0x3FFF) << 5)) | $rt)
  tbnz -> emit_u32(0x37000000 | ((($bit >> 5) & 0x1) << 31) | (($bit & 0x1F) << 19) | (((($offset >> 2) & 0x3FFF) << 5)) | $rt)
  cmp_rr -> emit_u32(0xEB00001F | ($rm << 16) | ($rn << 5))
  cmp_ri -> emit_u32(0xF100001F | (($imm & 0xFFF) << 10) | ($rn << 5))
  tst_rr -> emit_u32(0xEA00001F | ($rm << 16) | ($rn << 5))
  beq -> emit_u32(0x54000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | 0x0)
  bne -> emit_u32(0x54000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | 0x1)
  blt -> emit_u32(0x54000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | 0xB)
  bgt -> emit_u32(0x54000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | 0xC)
  ble -> emit_u32(0x54000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | 0xD)
  bge -> emit_u32(0x54000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | 0xA)
  blo -> emit_u32(0x54000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | 0x3)
  bhi -> emit_u32(0x54000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | 0x8)
  bls -> emit_u32(0x54000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | 0x9)
  bhs -> emit_u32(0x54000000 | (((($offset >> 2) & 0x7FFFF) << 5)) | 0x2)
  svc -> emit_u32(0xD4000001 | (($imm & 0xFFFF) << 5))
  nop -> emit_u32(0xD503201F)
  prologue -> emit_u32(0xA9BF7BFD), emit_u32(0x910003FD)
  epilogue -> emit_u32(0xA8C17BFD), emit_u32(0xD65F03C0)
B reg_encode: x0 | x1 | x2 | x3 | x4 | x5 | x6 | x7 | x8 | x9 | x10 | x11 | x12 | x13 | x14 | x15 | x16 | x17 | x18 | x19 | x20 | x21 | x22 | x23 | x24 | x25 | x26 | x27 | x28 | x29 | x30 | sp | xzr | wzr
  x0 -> set(reg_num, 0)
  x1 -> set(reg_num, 1)
  x2 -> set(reg_num, 2)
  x3 -> set(reg_num, 3)
  x4 -> set(reg_num, 4)
  x5 -> set(reg_num, 5)
  x6 -> set(reg_num, 6)
  x7 -> set(reg_num, 7)
  x8 -> set(reg_num, 8)
  x9 -> set(reg_num, 9)
  x10 -> set(reg_num, 10)
  x11 -> set(reg_num, 11)
  x12 -> set(reg_num, 12)
  x13 -> set(reg_num, 13)
  x14 -> set(reg_num, 14)
  x15 -> set(reg_num, 15)
  x16 -> set(reg_num, 16)
  x17 -> set(reg_num, 17)
  x18 -> set(reg_num, 18)
  x19 -> set(reg_num, 19)
  x20 -> set(reg_num, 20)
  x21 -> set(reg_num, 21)
  x22 -> set(reg_num, 22)
  x23 -> set(reg_num, 23)
  x24 -> set(reg_num, 24)
  x25 -> set(reg_num, 25)
  x26 -> set(reg_num, 26)
  x27 -> set(reg_num, 27)
  x28 -> set(reg_num, 28)
  x29 -> set(reg_num, 29)
  x30 -> set(reg_num, 30)
  sp -> set(reg_num, 31)
  xzr -> set(reg_num, 31)
  wzr -> set(reg_num, 31)
B reg_alias: fp | lr | ip0 | ip1 | pr
  fp -> set(reg_num, 29)
  lr -> set(reg_num, 30)
  ip0 -> set(reg_num, 16)
  ip1 -> set(reg_num, 17)
  pr -> set(reg_num, 18)

L encode_all: instructions -> output (deps=1)
L encode_one: instruction -> output (deps=1)

D instructions: N [input, sequential]
D output: M [output, sequential]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| instruction | add_rr \| add_ri \| sub_rr \| sub_ri \| adds_rr \| subs_rr \| and_rr \| and_ri \| orr_rr \| orr_ri \| eor_rr \| eor_ri \| mov_rr \| mov_ri \| movz \| movk \| movn \| ldr \| ldrb \| ldrh \| ldrsw \| ldrsb \| ldrsh \| str \| strb \| strh \| ldp \| stp \| b \| bl \| br \| blr \| ret \| cbz \| cbnz \| tbz \| tbnz \| cmp_rr \| cmp_ri \| tst_rr \| beq \| bne \| blt \| bgt \| ble \| bge \| blo \| bhi \| bls \| bhs \| svc \| nop \| prologue \| epilogue | topological |
| reg_encode | x0 \| x1 \| x2 \| x3 \| x4 \| x5 \| x6 \| x7 \| x8 \| x9 \| x10 \| x11 \| x12 \| x13 \| x14 \| x15 \| x16 \| x17 \| x18 \| x19 \| x20 \| x21 \| x22 \| x23 \| x24 \| x25 \| x26 \| x27 \| x28 \| x29 \| x30 \| sp \| xzr \| wzr | topological |
| reg_alias | fp \| lr \| ip0 \| ip1 \| pr | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| encode_all | instructions | output | 1 |  |
| encode_one | instruction | output | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| instructions | N | input, sequential |
| output | M | output, sequential |

## Returns

`output`
