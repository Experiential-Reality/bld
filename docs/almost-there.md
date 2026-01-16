# Almost There: BLD Self-Hosting

## The Three Primitives

| Primitive | Meaning | Compilation |
|-----------|---------|-------------|
| **B** (Boundary) | Partition, distinction | Conditional branch |
| **L** (Link) | Connection, relation | Data flow, sequence |
| **D** (Dimension) | Repetition, extension | Loop |

## The Cost Formula

```
Cost = B + D × L
```

Where:
- **B** = number of partitions (topological, invariant)
- **D** = extent of repetition (scales)
- **L** = -½ ln(1 - ρ²) where ρ = correlation strength

**Key insight**: D multiplies L, not B. Geometric properties scale with dimension; topological properties are invariant.

## The Problem We're Solving

We have two modes of traversal:

### 1. Execute Mode (what we have)
```
traverse(CLI) → executes emit("help text") → output buffer contains text
```

The traverser visits B/L/D and executes semantics immediately. When it sees `emit("hello")`, it appends "hello" to output.

### 2. Compile Mode (what we need)
```
compile(CLI) → generates code that will emit("help text") at runtime
```

The traverser visits B/L/D and generates code. When it sees `emit("hello")`, it generates:
```x86
mov rax, 1          ; syscall write
mov rdi, 1          ; stdout
mov rsi, hello_addr ; buffer
mov rdx, 5          ; length
syscall
```

## Structure IS Computation

This is literal. The CLI structure:

```bld
B command: parse | compile | run | cost
  parse -> uses=Parser
  compile -> uses=BLDCompiler
  run -> uses=Traverser
  cost -> uses=CostCalculator
```

When EXECUTED: visits partitions, runs semantics, produces output.

When COMPILED: becomes actual machine code:
```x86
; B command → conditional dispatch
  mov rsi, [argv+8]        ; argv[1]
  lea rdi, [str_parse]
  call strcmp
  test eax, eax
  jz .parse_handler

  lea rdi, [str_compile]
  call strcmp
  test eax, eax
  jz .compile_handler
  ; ... etc

.parse_handler:
  ; uses=Parser → code for Parser

.compile_handler:
  ; uses=BLDCompiler → code for BLDCompiler
```

## The Compilation Pipeline

```
bld compile --from bld --to linux,x86,elf cli.bld bin/bld
```

Each stage is a structure that transforms:

```
cli.bld (source)
    ↓ parse
ParsedStructure { boundaries, links, dimensions }
    ↓ linux.bld
Linux operations { entry, read_argc, read_argv, strcmp, syscall_* }
    ↓ x86.bld
Machine code bytes { 48 89 e5 ... }
    ↓ elf.bld
ELF binary { 7f 45 4c 46 ... }
```

## What Each Structure Contributes

### linux.bld
- Entry point (program_start)
- argc/argv access (read_argc, read_argv)
- String operations (strcmp)
- System calls (syscall_write, syscall_read, syscall_exit)

### x86.bld
- Instruction encoding (mov, cmp, jmp, call, syscall)
- Register allocation
- ModRM/SIB/REX byte composition

### elf.bld
- ELF header (magic, class, machine type)
- Program headers (load segments)
- Entry point address

## The Missing Piece

Currently, when we "compile" CLI:

```python
# Trace mode: capture what CLI emits
t.state.set('mode_trace', 'record')
t.traverse(cli)  # → trace = ["help text line 1", "help text line 2", ...]

# Compile trace: wrap in syscall_write
t.traverse(Trace)  # → ELF that prints help
```

This compiles the OUTPUT of CLI, not the STRUCTURE of CLI.

For self-hosting, we need:

```python
# Compile mode: generate code for CLI's structure
t.state.set('mode_compile', 'codegen')
t.traverse(cli)  # → generates dispatch code, handlers, etc.
```

When visiting `B command: parse | compile | ...`:
- Don't select a partition to execute
- Generate code that will select at runtime based on argv[1]

When visiting `emit("text")`:
- Don't emit text to output buffer
- Generate syscall_write code that will emit at runtime

## The Math of Compilation

Compilation preserves structure:

```
Cost(source) ≈ Cost(compiled)
```

The B/L/D of the source maps to B/L/D of the output:
- B (partitions) → conditional branches
- L (connections) → instruction sequences
- D (repetitions) → loops

The cost formula applies to both:
- Source: `Cost = B_partitions + D_iterations × L_deps`
- Compiled: `Cost = B_branches + D_loops × L_instructions`

## Almost There

We have:
- ✓ Parser (bld → ParsedStructure)
- ✓ Trace mode (capture emits)
- ✓ Lowering (operations → x86)
- ✓ ELF generation (code → binary)
- ✓ CLI structure with command dispatch

We need:
- Compile mode in traverser (structure → code, not structure → output)
- The insight: B/L/D ARE control flow, compile them as such

The traverser already knows HOW to visit B/L/D. We just need to change WHAT it does:
- Execute mode: run semantics immediately
- Compile mode: emit code that runs semantics at runtime

This is the final step. The structure IS the program. Compile the structure, get the program.
