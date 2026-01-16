# BLDGrammar

**Cost**: B + D×L = 41 + 1×1.438 = 42.438

---

## Structure

```
structure BLDGrammar

B file_element: structure_decl | comment | blank
  structure_decl -> keyword("structure"), whitespace, identifier
  comment -> char("#"), skip_to_eol
  blank -> only_whitespace
B decl_type: boundary | link | dimension | parameter | returns | semantic_line | comment
  boundary -> keyword("B"), whitespace, identifier, colon, partitions
  link -> keyword("L"), whitespace, identifier, colon, flow
  dimension -> keyword("D"), whitespace, identifier, colon, extent
  parameter -> keyword("P"), whitespace, identifier, colon, type
  returns -> keyword("returns"), colon, type
  semantic_line -> indent, identifier, arrow, semantic_content
  comment -> char("#"), skip_to_eol
B token: keyword | identifier | number | string | symbol | newline | indent | dedent | eof
  keyword -> one_of("structure", "B", "L", "D", "P", "returns")
  identifier -> regex([a-zA-Z_][a-zA-Z0-9_]*)
  number -> regex([0-9]+)
  string -> char('"'), content, char('"')
  symbol -> one_of(":", "|", "->", "[", "]", "(", ")", ",", "=")
  newline -> char('\n')
  indent -> spaces_gt_current
  dedent -> spaces_lt_current
  eof -> end_of_input
B extent_type: fixed | symbolic | computed
  fixed -> number
  symbolic -> identifier
  computed -> expr_with_ops
B prop_category: execution | io | memory | typing | scalar
  execution -> one_of("parallel", "sequential")
  io -> one_of("input", "output")
  memory -> one_of("contiguous", "stride")
  typing -> keyword("type"), equals, identifier
  scalar -> keyword("scalar"), optional(type_annotation)
B link_attr: deps | pattern | engine | uses | rho | count | ops | scaling
  deps -> keyword("deps"), equals, number
  pattern -> one_of("coalesced", "scatter", "broadcast", "reduce")
  engine -> one_of("memory", "compute", "copy")
  uses -> keyword("uses"), equals, identifier
  rho -> keyword("rho"), equals, number
  count -> keyword("count"), equals, number
  ops -> keyword("ops"), equals, number
  scaling -> one_of("per_block", "per_chunk")
B semantic_type: pattern_match | text_match | action | emit | next_state | compose
  pattern_match -> keyword("pattern"), paren_content
  text_match -> keyword("text_match"), paren_content
  action -> keyword("action"), paren_content
  emit -> keyword("emit_kind"), paren_content
  next_state -> keyword("next_state"), paren_content
  compose -> keyword("uses"), paren_content

L file_parse: source -> structures (deps=0)
L structure_parse: keyword_structure -> name -> body (deps=1)
L body_parse: newline -> declarations (deps=1)
L boundary_parse: B -> name -> colon -> partitions (deps=1)
L link_parse: L -> name -> colon -> from -> arrow -> to -> attrs (deps=1)
L dimension_parse: D -> name -> colon -> extent -> props (deps=1)
L parameter_parse: P -> name -> colon -> type -> props (deps=1)
L returns_parse: returns -> colon -> type (deps=1)
L partitions_parse: partition -> pipe_partition* (deps=0)
L partition_item: identifier -> semantics? (deps=0)
L props_parse: bracket_open -> prop_list -> bracket_close (deps=1)
L prop_list: prop -> comma_prop* (deps=0)
L attrs_parse: paren_open -> attr_list -> paren_close (deps=1)
L attr_list: attr -> comma_attr* (deps=0)
L semantic_parse: indent -> key -> arrow -> value (deps=1)
L semantic_content: key_value -> comma_key_value* (deps=0)

D structures: N [parallel]
D declarations: M [parallel]
D partitions: K [parallel]
D properties: P [parallel]
D semantics: S [parallel]
D attributes: A [parallel]

returns: ParsedBLDFile
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| file_element | structure_decl \| comment \| blank | topological |
| decl_type | boundary \| link \| dimension \| parameter \| returns \| semantic_line \| comment | topological |
| token | keyword \| identifier \| number \| string \| symbol \| newline \| indent \| dedent \| eof | topological |
| extent_type | fixed \| symbolic \| computed | topological |
| prop_category | execution \| io \| memory \| typing \| scalar | topological |
| link_attr | deps \| pattern \| engine \| uses \| rho \| count \| ops \| scaling | topological |
| semantic_type | pattern_match \| text_match \| action \| emit \| next_state \| compose | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| file_parse | source | structures | 0 |  |
| structure_parse | keyword_structure | name -> body | 1 |  |
| body_parse | newline | declarations | 1 |  |
| boundary_parse | B | name -> colon -> partitions | 1 |  |
| link_parse | L | name -> colon -> from -> arrow -> to -> attrs | 1 |  |
| dimension_parse | D | name -> colon -> extent -> props | 1 |  |
| parameter_parse | P | name -> colon -> type -> props | 1 |  |
| returns_parse | returns | colon -> type | 1 |  |
| partitions_parse | partition | pipe_partition* | 0 |  |
| partition_item | identifier | semantics? | 0 |  |
| props_parse | bracket_open | prop_list -> bracket_close | 1 |  |
| prop_list | prop | comma_prop* | 0 |  |
| attrs_parse | paren_open | attr_list -> paren_close | 1 |  |
| attr_list | attr | comma_attr* | 0 |  |
| semantic_parse | indent | key -> arrow -> value | 1 |  |
| semantic_content | key_value | comma_key_value* | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| structures | N | parallel |
| declarations | M | parallel |
| partitions | K | parallel |
| properties | P | parallel |
| semantics | S | parallel |
| attributes | A | parallel |

## Returns

`ParsedBLDFile`
