# RustEmitter

**Cost**: B + D×L = 13 + 1×1.582 = 14.582

---

## Structure

```
structure RustEmitter

B emit_phase: imports | enums | struct_def | impl_block | main_fn
  imports -> order(1)
  enums -> order(2), foreach(boundary)
  struct_def -> order(3)
  impl_block -> order(4)
  main_fn -> order(5)
B ownership: borrowed | mutable | owned
  borrowed -> rust_type(&T)
  mutable -> rust_type(&mut T)
  owned -> rust_type(T)
B visibility: pub | private
  pub -> prefix("pub ")
  private -> prefix("")
B returns: void | value | result
  void -> return_type("()")
  value -> return_type(T)
  result -> return_type("Result<T, E>")

L emit_imports: unit -> imports (deps=1)
L emit_enum: boundary -> enums (deps=1)
L emit_struct: dimensions -> struct_def (deps=1)
L emit_impl: links -> impl_block (deps=1)
L emit_main: pattern -> main_fn (deps=1)
L method_signature: link -> signature (deps=0)
L method_body: link -> body (deps=1)
L emit_call: link -> call_expr (deps=0)
L emit_line: text -> output (deps=1)
L indent: indent_level -> indent_level (deps=1)
L dedent: indent_level -> indent_level (deps=1)
L blank: unit -> output (deps=1)
L assemble: sections -> output (deps=1)

D parsed: 1 [input, type=ParsedStructure]
D pattern: 1 [input]
D output: N [output, sequential]
D imports: M [sequential]
D enums: M [sequential]
D struct_def: M [sequential]
D impl_block: M [sequential]
D main_fn: M [sequential]
D indent_level: 1 [sequential]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| emit_phase | imports \| enums \| struct_def \| impl_block \| main_fn | topological |
| ownership | borrowed \| mutable \| owned | topological |
| visibility | pub \| private | topological |
| returns | void \| value \| result | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| emit_imports | unit | imports | 1 |  |
| emit_enum | boundary | enums | 1 |  |
| emit_struct | dimensions | struct_def | 1 |  |
| emit_impl | links | impl_block | 1 |  |
| emit_main | pattern | main_fn | 1 |  |
| method_signature | link | signature | 0 |  |
| method_body | link | body | 1 |  |
| emit_call | link | call_expr | 0 |  |
| emit_line | text | output | 1 |  |
| indent | indent_level | indent_level | 1 |  |
| dedent | indent_level | indent_level | 1 |  |
| blank | unit | output | 1 |  |
| assemble | sections | output | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| parsed | 1 | input, type=ParsedStructure |
| pattern | 1 | input |
| output | N | output, sequential |
| imports | M | sequential |
| enums | M | sequential |
| struct_def | M | sequential |
| impl_block | M | sequential |
| main_fn | M | sequential |
| indent_level | 1 | sequential |

## Returns

`output`
