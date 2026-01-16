# MarkdownEmitter
> **Status**: VALIDATED

**Cost**: B + D×L = 25 + 7×1.295 = 34.062

---

## Structure

```
structure MarkdownEmitter

B section_type: header | drawing | boundaries | links | dimensions | cost | returns
  header -> emit_title, emit_status, emit_insight
  drawing -> emit_code_block, content(parse_output)
  boundaries -> emit_table, cols([name), partitions, properties]
  links -> emit_table, cols([name), source, target, deps, attrs]
  dimensions -> emit_table, cols([name), extent, properties]
  cost -> emit_formula
  returns -> emit_inline_code
B emit_type: title | table | code_block | formula | text
  title -> emit_bytes("# "), emit_name, emit_bytes("\n\n")
  table -> emit_header_row, emit_separator, emit_data_rows
  code_block -> emit_bytes("```\n"), emit_content, emit_bytes("```\n")
  formula -> emit_bytes("**Cost**: "), emit_cost_string, emit_bytes("\n")
  text -> emit_paragraph
B table_col: name | partitions | source | target | deps | attrs | extent | properties
  name -> align(left), width(variable)
  partitions -> align(left), join(" | ")
  source -> align(left)
  target -> align(left)
  deps -> align(right)
  attrs -> align(left), join("), "
  extent -> align(right)
  properties -> align(left), join("), "
B status_type: validated | derived | exploratory | foundational | mixed
  validated -> emit_bytes("> **Status**: VALIDATED\n\n")
  derived -> emit_bytes("> **Status**: Derived\n\n")
  exploratory -> emit_bytes("> **Status**: Exploratory\n\n")
  foundational -> emit_bytes("> **Status**: Foundational\n\n")
  mixed -> emit_bytes("> **Status**: Mixed\n\n")

L traverse: structure -> output (deps=1)
L order: header -> cost -> drawing -> boundaries -> links -> dimensions -> returns (deps=1, sequential=true)
L emit_header: structure.name -> output (deps=0)
L detect_status: structure.comments -> status_type (deps=0)
L emit_status: status_type -> output (deps=1)
L format_drawing: structure -> string (deps=1)
L emit_drawing: string -> output (deps=1)
L emit_table_header: cols -> output (deps=0)
L emit_table_sep: cols -> output (deps=0)
L emit_table_rows: elements -> output (deps=1)
L format_cell: element.field -> string (deps=0)
L join_cells: cells -> row (deps=1, separator=" | ")
L calculate_cost: structure -> cost (deps=1)
L format_cost: cost -> string (deps=1, template="B + D×L = {b} + {d}×{l} = {total}")
L emit_returns: structure.returns -> output (deps=0)

D structure: 1 [input, type=ParsedStructure]
D output: N [output, type=String]
D position: 1 [sequential]
D indent: 1 [sequential]
D sections: 7 [sequential, ordered]
D boundaries: N [parallel, from=structure.boundaries]
D links: N [parallel, from=structure.links]
D dimensions: N [parallel, from=structure.dimensions]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| section_type | header \| drawing \| boundaries \| links \| dimensions \| cost \| returns | topological |
| emit_type | title \| table \| code_block \| formula \| text | topological |
| table_col | name \| partitions \| source \| target \| deps \| attrs \| extent \| properties | topological |
| status_type | validated \| derived \| exploratory \| foundational \| mixed | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| traverse | structure | output | 1 |  |
| order | header | cost -> drawing -> boundaries -> links -> dimensions -> returns | 1 | sequential=true |
| emit_header | structure.name | output | 0 |  |
| detect_status | structure.comments | status_type | 0 |  |
| emit_status | status_type | output | 1 |  |
| format_drawing | structure | string | 1 |  |
| emit_drawing | string | output | 1 |  |
| emit_table_header | cols | output | 0 |  |
| emit_table_sep | cols | output | 0 |  |
| emit_table_rows | elements | output | 1 |  |
| format_cell | element.field | string | 0 |  |
| join_cells | cells | row | 1 | separator=" | " |
| calculate_cost | structure | cost | 1 |  |
| format_cost | cost | string | 1 | template="B + D×L = {b} + {d}×{l} = {total}" |
| emit_returns | structure.returns | output | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| structure | 1 | input, type=ParsedStructure |
| output | N | output, type=String |
| position | 1 | sequential |
| indent | 1 | sequential |
| sections | 7 | sequential, ordered |
| boundaries | N | parallel, from=structure.boundaries |
| links | N | parallel, from=structure.links |
| dimensions | N | parallel, from=structure.dimensions |

## Returns

`output`
