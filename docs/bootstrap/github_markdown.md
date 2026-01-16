# GitHubMarkdownEmitter

**Cost**: B + D×L = 42 + 150×1.295 = 236.185

---

## Structure

```
structure GitHubMarkdownEmitter

B section_type: header | alerts | diagram | drawing | boundaries | links | dimensions | cost | returns | footer
  header -> emit_title, emit_badges, emit_toc
  alerts -> emit_status_alert, emit_cost_alert
  diagram -> emit_mermaid, type(flowchart)
  drawing -> emit_collapsible, title("BLD Structure"), content(parse_output)
  boundaries -> emit_table, cols([name), partitions, properties]
  links -> emit_table, cols([name), source, target, deps, attrs]
  dimensions -> emit_table, cols([name), extent, properties]
  cost -> emit_formula
  returns -> emit_inline_code
  footer -> emit_generated_by, emit_links
B alert_type: note | tip | important | warning | caution
  note -> emit_bytes("> [!NOTE]\n> "), color(blue)
  tip -> emit_bytes("> [!TIP]\n> "), color(green)
  important -> emit_bytes("> [!IMPORTANT]\n> "), color(purple)
  warning -> emit_bytes("> [!WARNING]\n> "), color(yellow)
  caution -> emit_bytes("> [!CAUTION]\n> "), color(red)
B status_to_alert: validated | derived | exploratory | foundational | mixed
  validated -> alert(tip), message("This structure is empirically validated.")
  derived -> alert(note), message("This structure is mathematically derived.")
  exploratory -> alert(warning), message("This structure is exploratory - not yet validated.")
  foundational -> alert(important), message("This is a foundational BLD structure.")
  mixed -> alert(note), message("Validation status varies by component.")
B diagram_type: flowchart | graph | stateDiagram
  flowchart -> direction(TD), show_B_L_D
  graph -> direction(LR), show_dependencies
  stateDiagram -> show_partitions
B mermaid_node: boundary_node | link_node | dimension_node | partition_node
  boundary_node -> shape("[[ ]]"), style(boundary)
  link_node -> style(link)
  dimension_node -> shape("[/ /]"), style(dimension)
  partition_node -> shape("[ ]"), style(partition)
B collapsible: collapsed | expanded
  collapsed -> emit_bytes("<details>\n<summary>"), emit_title, emit_bytes("</summary>\n\n")
  expanded -> emit_bytes("<details open>\n<summary>"), emit_title, emit_bytes("</summary>\n\n")
B badge_type: status_badge | cost_badge | domain_badge
  status_badge -> url("https://img.shields.io/badge/status-{status}-{color}")
  cost_badge -> url("https://img.shields.io/badge/cost-{cost}-blue")
  domain_badge -> url("https://img.shields.io/badge/domain-{domain}-purple")
B toc_entry: toc_structure | toc_boundaries | toc_links | toc_dimensions | toc_cost
  toc_structure -> anchor("#structure"), level(2)
  toc_boundaries -> anchor("#boundaries-b"), level(2)
  toc_links -> anchor("#links-l"), level(2)
  toc_dimensions -> anchor("#dimensions-d"), level(2)
  toc_cost -> anchor("#cost"), level(2)
B split_decision: inline | split_file
  inline -> cost_below_threshold, emit_inline
  split_file -> cost_above_threshold, emit_uses_reference, create_subfile
B split_threshold: human | claude | custom
  human -> threshold(4), working_memory_limit
  claude -> threshold(100), context_optimization
  custom -> threshold(N), user_specified

L close_collapsible: content -> output_text (deps=1, suffix="\n</details>\n")
L emit_badge: badge_type -> output_text (deps=0, format="![{label}]({url})")
L emit_toc: sections -> output_text (deps=0, format="- [{title}]({anchor})")
L check_cost: sub_structure -> split_decision (deps=1)
L emit_reference: sub_structure -> uses_link (deps=0, format="uses={path}")
L create_file: sub_structure -> file_path (deps=1)
L traverse: input_structure -> output_text (deps=1)
L order: header -> alerts -> diagram -> drawing -> boundaries -> links -> dimensions -> cost -> returns -> footer (deps=1, sequential=true)
L generate_mermaid: input_structure -> diagram (deps=1)
L emit_mermaid_header: diagram_type -> output_text (deps=0, prefix="```mermaid\n")
L emit_mermaid_nodes: elements -> output_text (deps=1)
L emit_mermaid_edges: links -> output_text (deps=1)
L emit_mermaid_footer:  -> output_text (deps=0, suffix="```\n")
L detect_status: input_structure.comments -> status (deps=0)
L format_badge_url: status -> url (deps=1)
L emit_footer:  -> output_text (deps=0)

D input_structure: 1 [input, type=ParsedStructure]
D output_text: N [output, type=String]
D sub_structures: N [parallel, from=input_structure.uses]
D output_files: M [parallel, created_on_split]
D sections: 10 [sequential, ordered]
D boundaries: N [parallel, from=input_structure.boundaries]
D links: N [parallel, from=input_structure.links]
D dimensions: N [parallel, from=input_structure.dimensions]
D toc_entries: 5 [sequential]
D badges: 3 [parallel]

returns: output_text
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| section_type | header \| alerts \| diagram \| drawing \| boundaries \| links \| dimensions \| cost \| returns \| footer | topological |
| alert_type | note \| tip \| important \| warning \| caution | topological |
| status_to_alert | validated \| derived \| exploratory \| foundational \| mixed | topological |
| diagram_type | flowchart \| graph \| stateDiagram | topological |
| mermaid_node | boundary_node \| link_node \| dimension_node \| partition_node | topological |
| collapsible | collapsed \| expanded | topological |
| badge_type | status_badge \| cost_badge \| domain_badge | topological |
| toc_entry | toc_structure \| toc_boundaries \| toc_links \| toc_dimensions \| toc_cost | topological |
| split_decision | inline \| split_file | topological |
| split_threshold | human \| claude \| custom | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| close_collapsible | content | output_text | 1 | suffix="\n</details>\n" |
| emit_badge | badge_type | output_text | 0 | format="![{label}]({url})" |
| emit_toc | sections | output_text | 0 | format="- [{title}]({anchor})" |
| check_cost | sub_structure | split_decision | 1 |  |
| emit_reference | sub_structure | uses_link | 0 | format="uses={path}" |
| create_file | sub_structure | file_path | 1 |  |
| traverse | input_structure | output_text | 1 |  |
| order | header | alerts -> diagram -> drawing -> boundaries -> links -> dimensions -> cost -> returns -> footer | 1 | sequential=true |
| generate_mermaid | input_structure | diagram | 1 |  |
| emit_mermaid_header | diagram_type | output_text | 0 | prefix="```mermaid\n" |
| emit_mermaid_nodes | elements | output_text | 1 |  |
| emit_mermaid_edges | links | output_text | 1 |  |
| emit_mermaid_footer |  | output_text | 0 | suffix="```\n" |
| detect_status | input_structure.comments | status | 0 |  |
| format_badge_url | status | url | 1 |  |
| emit_footer |  | output_text | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| input_structure | 1 | input, type=ParsedStructure |
| output_text | N | output, type=String |
| sub_structures | N | parallel, from=input_structure.uses |
| output_files | M | parallel, created_on_split |
| sections | 10 | sequential, ordered |
| boundaries | N | parallel, from=input_structure.boundaries |
| links | N | parallel, from=input_structure.links |
| dimensions | N | parallel, from=input_structure.dimensions |
| toc_entries | 5 | sequential |
| badges | 3 | parallel |

## Returns

`output_text`
