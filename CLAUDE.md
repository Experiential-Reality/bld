# Claude Instructions for BLD

This repository contains the BLD (Boundary/Link/Dimension) language and interpreter.

## Core Principle

**Structure IS computation.** The interpreter traverses BLD structures to produce output.

## The Three Primitives

| Primitive | Meaning | Question |
|-----------|---------|----------|
| **B** (Boundary) | Partition, distinction | Where does behavior partition? |
| **L** (Link) | Connection, relation | What connects to what? |
| **D** (Dimension) | Repetition, extension | What repeats? |

## Key Insight: D×L Scaling

D multiplies L, not B.
- Geometric properties (L) scale with dimension
- Topological properties (B) are invariant

## Repository Structure

```
bld/
├── src/bld/           # Python interpreter (MINIMAL)
│   ├── parser.py      # Parse .bld text
│   └── traverser.py   # Execute by traversal
├── bootstrap/         # Self-describing .bld files
│   ├── bld.bld        # BLD language spec (self-referential)
│   ├── x86.bld        # x86 encoding as BLD
│   ├── elf.bld        # ELF format as BLD
│   └── ...
├── examples/          # Example structures
│   ├── functional/    # map, fold, filter
│   ├── blas/          # Linear algebra
│   └── ai/            # Neural network ops
└── .claude/skills/bld/  # Claude skill files
```

## The Interpreter

The Python interpreter is MINIMAL. It only implements:

1. **Parse** - .bld text → structure
2. **Traverse** - Visit B/L/D, execute semantics
3. **Primitives** - emit_byte, set, get, modrm, rex, etc.

Everything else (x86 encoding, ELF format, etc.) is written IN BLD and executed by the interpreter.

## Semantic Primitives

The interpreter understands these primitive operations:

| Primitive | Purpose |
|-----------|---------|
| `emit_byte(x)` | Emit single byte |
| `emit_bytes(...)` | Emit multiple bytes |
| `emit_u16/u32/u64(x)` | Emit little-endian integer |
| `set(name, val)` | Set state variable |
| `get(name)` | Get state variable |
| `label(name)` | Define label at current position |
| `reloc(name)` | Emit relocation placeholder |
| `modrm(mod, reg, rm)` | Emit ModR/M byte |
| `rex(w, r, x, b)` | Emit REX prefix |

## Alignment Cost

```
Cost = B_cost + D × L_cost
```

When structures align, cost is minimized.

## The /bld Skill

A `/bld` skill is available in `.claude/skills/bld/` with domain-specific guides.

## Remember

> "The structure you find is the structure that exists. BLD doesn't impose—it reveals."
