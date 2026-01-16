# Parser

**Cost**: B + D×L = 19 + 1×1.582 = 20.582

---

## Structure

```
structure Parser

B line_type: structure_start | B_decl | L_decl | D_decl | P_decl | returns_line | comment | blank | eof
  structure_start -> keyword_match("structure")
  B_decl -> keyword_match("B")
  L_decl -> keyword_match("L")
  D_decl -> keyword_match("D")
  P_decl -> keyword_match("P")
  returns_line -> keyword_match("returns")
  eof -> token_kind(Eof)
B parse_state: top_level | in_structure | after_returns | error
  top_level -> initial_state, expect(structure_start)
  in_structure -> accept(B_decl, L_decl, D_decl, P_decl, returns_line)
  after_returns -> accept(eof, structure_start)
  error -> terminal_state
B prop_state: before_props | in_props | after_props
  before_props -> expect(bracket_open)
  in_props -> accept(identifier, comma)
  after_props -> expect(bracket_close)
B sync_state: synced | recovering | failed
  synced -> continue_parsing
  recovering -> skip_to_sync_point, consume_until(newline | structure_start)
  failed -> emit_errors, return_partial_ast

L peek: tokens -> token (deps=0)
L consume: position -> token (deps=1)
L expect: token -> token (deps=1)
L classify_line: token -> line_type (deps=0)
L parse_boundary: tokens -> boundary (deps=1)
L parse_link: tokens -> link (deps=1)
L parse_dimension: tokens -> dimension (deps=1)
L parse_parameter: tokens -> parameter (deps=1)
L parse_returns: tokens -> return_type (deps=1)
L dispatch: line_type -> decl (deps=1)
L add_decl: decl -> current_structure (deps=1)
L finalize: current_structure -> parsed (deps=1)
L parse_properties: tokens -> properties (deps=1)

D tokens: N [input, type=Token]
D parsed: 1 [output, type=ParsedStructure]
D position: 1 [sequential]
D current_structure: 1 [sequential]

returns: ParsedStructure
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| line_type | structure_start \| B_decl \| L_decl \| D_decl \| P_decl \| returns_line \| comment \| blank \| eof | topological |
| parse_state | top_level \| in_structure \| after_returns \| error | topological |
| prop_state | before_props \| in_props \| after_props | topological |
| sync_state | synced \| recovering \| failed | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| peek | tokens | token | 0 |  |
| consume | position | token | 1 |  |
| expect | token | token | 1 |  |
| classify_line | token | line_type | 0 |  |
| parse_boundary | tokens | boundary | 1 |  |
| parse_link | tokens | link | 1 |  |
| parse_dimension | tokens | dimension | 1 |  |
| parse_parameter | tokens | parameter | 1 |  |
| parse_returns | tokens | return_type | 1 |  |
| dispatch | line_type | decl | 1 |  |
| add_decl | decl | current_structure | 1 |  |
| finalize | current_structure | parsed | 1 |  |
| parse_properties | tokens | properties | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| tokens | N | input, type=Token |
| parsed | 1 | output, type=ParsedStructure |
| position | 1 | sequential |
| current_structure | 1 | sequential |

## Returns

`ParsedStructure`
