# Tokenizer

**Cost**: B + D×L = 43 + 16×0.719 = 54.507

---

## Structure

```
structure Tokenizer

B char_class: whitespace | alpha | digit | symbol | hash | colon | pipe | newline | quote | bracket_open | bracket_close | paren_open | paren_close | comma | equals | arrow_start | eof
  whitespace -> pattern(b' ' | b'\t' | b'\r')
  alpha -> pattern(b'a'..=b'z' | b'A'..=b'Z' | b'_')
  digit -> pattern(b'0'..=b'9')
  symbol -> pattern(b'.' | b'*' | b'+' | b'/' | b'%' | b'&' | b'!' | b'?' | b'@' | b'^' | b'~' | b'`' | b';')
  hash -> pattern(b'#')
  colon -> pattern(b':')
  pipe -> pattern(b'|')
  newline -> pattern(b'\n')
  quote -> pattern(b'"')
  bracket_open -> pattern(b'[')
  bracket_close -> pattern(b']')
  paren_open -> pattern(b'(')
  paren_close -> pattern(b')')
  comma -> pattern(b',')
  equals -> pattern(b'=')
  arrow_start -> pattern(b'-')
  eof -> pattern(0)
B state: line_start | in_line | in_identifier | in_number | in_string | in_comment | at_eof
  line_start -> initial_state
  in_line -> default_state
  in_identifier -> accumulate_state
  in_number -> accumulate_state
  in_string -> accumulate_until(quote)
  in_comment -> skip_until(newline)
  at_eof -> terminal_state
B transition: stay | goto_line | goto_identifier | goto_number | goto_string | goto_comment | goto_eof
  stay -> next_state(same)
  goto_line -> next_state(in_line)
  goto_identifier -> next_state(in_identifier), action(start_token)
  goto_number -> next_state(in_number), action(start_token)
  goto_string -> next_state(in_string), action(start_token)
  goto_comment -> next_state(in_comment)
  goto_eof -> next_state(at_eof), action(emit_eof)
B emit: yes | no
  yes -> action(emit_token)
  no -> action(skip)
B keyword_match: structure_kw | B_kw | L_kw | D_kw | P_kw | returns_kw | not_keyword
  structure_kw -> text_match("structure"), emit_kind(keyword)
  B_kw -> text_match("B"), emit_kind(keyword)
  L_kw -> text_match("L"), emit_kind(keyword)
  D_kw -> text_match("D"), emit_kind(keyword)
  P_kw -> text_match("P"), emit_kind(keyword)
  returns_kw -> text_match("returns"), emit_kind(keyword)
  not_keyword -> emit_kind(identifier)
B error_mode: normal | error_recovery | panic
  normal -> continue_tokenizing
  error_recovery -> skip_to_sync_point, emit_error_token
  panic -> stop_immediately, report_error

L classify: input -> char_class (deps=0)
L transition: state -> state (deps=1)
L accumulate: char -> token_text (deps=1)
L emit_token: token_text -> tokens (deps=1)
L track_indent: whitespace -> current_indent (deps=1)
L check_indent: indent_stack -> indent_tokens (deps=1)
L match_keyword: token_text -> keyword_match (deps=0)

D input: N [input, contiguous]
D tokens: M [output, type=Token]
D token_start: 1 [sequential]
D token_text: N [sequential]
D current_line: 1 [sequential]
D current_column: 1 [sequential]
D current_indent: 1 [sequential]
D indent_stack: 16 [sequential]

returns: tokens
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| char_class | whitespace \| alpha \| digit \| symbol \| hash \| colon \| pipe \| newline \| quote \| bracket_open \| bracket_close \| paren_open \| paren_close \| comma \| equals \| arrow_start \| eof | topological |
| state | line_start \| in_line \| in_identifier \| in_number \| in_string \| in_comment \| at_eof | topological |
| transition | stay \| goto_line \| goto_identifier \| goto_number \| goto_string \| goto_comment \| goto_eof | topological |
| emit | yes \| no | topological |
| keyword_match | structure_kw \| B_kw \| L_kw \| D_kw \| P_kw \| returns_kw \| not_keyword | topological |
| error_mode | normal \| error_recovery \| panic | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| classify | input | char_class | 0 |  |
| transition | state | state | 1 |  |
| accumulate | char | token_text | 1 |  |
| emit_token | token_text | tokens | 1 |  |
| track_indent | whitespace | current_indent | 1 |  |
| check_indent | indent_stack | indent_tokens | 1 |  |
| match_keyword | token_text | keyword_match | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| input | N | input, contiguous |
| tokens | M | output, type=Token |
| token_start | 1 | sequential |
| token_text | N | sequential |
| current_line | 1 | sequential |
| current_column | 1 | sequential |
| current_indent | 1 | sequential |
| indent_stack | 16 | sequential |

## Returns

`tokens`
