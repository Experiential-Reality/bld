# BLDProductions

**Cost**: B + D×L = 28 + 1×1.870 = 29.870

---

## Structure

```
structure BLDProductions

B file_content: structure | comment | blank
B declaration: B_decl | L_decl | D_decl | P_decl | returns_decl | semantic | comment
B extent: number | identifier | expression
B property: parallel | sequential | input | output | contiguous | scalar | type_spec | stride
B attribute: deps_attr | pattern_attr | engine_attr | uses_attr | rho_attr | count_attr | ops_attr

L file: epsilon -> structures (deps=0)
L structure_prod: structure_kw -> body (deps=1)
L body: newline -> declarations (deps=1)
L B_decl: B_kw -> partition_list (deps=1)
L partition_list: partition -> partitions (deps=0)
L partition: identifier -> name (deps=0)
L pipe_partition: pipe -> partition (deps=1)
L semantic_block: indent -> semantics (deps=1)
L semantic_line: identifier -> semantic_content (deps=1)
L L_decl: L_kw -> flow (deps=1)
L attr_block: paren_open -> attributes (deps=1)
L attr_list: attr -> attributes (deps=0)
L attr: identifier -> value (deps=1)
L D_decl: D_kw -> extent (deps=1)
L prop_block: bracket_open -> properties (deps=1)
L prop_list: property -> properties (deps=0)
L P_decl: P_kw -> type (deps=1)
L returns_decl: returns_kw -> type (deps=1)

D structures: N [parallel]
D declarations: M [parallel]
D partitions: K [parallel]
D properties: P [parallel]
D attributes: A [parallel]
D semantics: S [parallel]

returns: Grammar
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| file_content | structure \| comment \| blank | topological |
| declaration | B_decl \| L_decl \| D_decl \| P_decl \| returns_decl \| semantic \| comment | topological |
| extent | number \| identifier \| expression | topological |
| property | parallel \| sequential \| input \| output \| contiguous \| scalar \| type_spec \| stride | topological |
| attribute | deps_attr \| pattern_attr \| engine_attr \| uses_attr \| rho_attr \| count_attr \| ops_attr | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| file | epsilon | structures | 0 |  |
| structure_prod | structure_kw | body | 1 |  |
| body | newline | declarations | 1 |  |
| B_decl | B_kw | partition_list | 1 |  |
| partition_list | partition | partitions | 0 |  |
| partition | identifier | name | 0 |  |
| pipe_partition | pipe | partition | 1 |  |
| semantic_block | indent | semantics | 1 |  |
| semantic_line | identifier | semantic_content | 1 |  |
| L_decl | L_kw | flow | 1 |  |
| attr_block | paren_open | attributes | 1 |  |
| attr_list | attr | attributes | 0 |  |
| attr | identifier | value | 1 |  |
| D_decl | D_kw | extent | 1 |  |
| prop_block | bracket_open | properties | 1 |  |
| prop_list | property | properties | 0 |  |
| P_decl | P_kw | type | 1 |  |
| returns_decl | returns_kw | type | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| structures | N | parallel |
| declarations | M | parallel |
| partitions | K | parallel |
| properties | P | parallel |
| attributes | A | parallel |
| semantics | S | parallel |

## Returns

`Grammar`
