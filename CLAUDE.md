# Claude Instructions for BLD

This repository contains the BLD (Boundary/Link/Dimension) language and interpreter.

## Core Principle

**Structure IS computation.** The traverser composes BLD structures to produce output.

**BLD is metaprogramming.** It describes how to create anything for a specific well-understood traverser.

## What is a Traverser?

**The reader IS the traverser.** You reading this file are traversing it. An x86 chip executing binary is traversing 0..1 space.

| Traverser | What it traverses | Output |
|-----------|-------------------|--------|
| Human | .bld text | Understanding |
| bld-py | .bld structure | Bytes |
| x86 chip | Binary (0..1) | Computation |

**Empty traverser = implicit.** When no traverser is specified, whatever is reading IS the traverser.

**Traverser models** describe HOW a specific traverser processes structure:
- `traverser/x86.bld` - how x86 processes BLD structure
- When composed with a program, produces x86 machine code
- That machine code is then traversed by the x86 chip

### The Self-Hosting Flow

1. **BLD structure** (`program/cli.bld`) - describes WHAT
2. **Traverser model** (`traverser/x86.bld`) - describes HOW x86 processes it
3. **Pure traverser** (bld-py) composes both → x86 machine code
4. **Target traverser** (x86 chip) executes it
5. That binary can compose BLD for x86 → self-hosting

## The Three Primitives

| Primitive | Meaning | Question |
|-----------|---------|----------|
| **B** (Boundary) | Partition, distinction | Where does behavior partition? |
| **L** (Link) | Connection, composition | What connects to what? |
| **D** (Dimension) | Repetition, positions | What repeats? |

## Key Insights

**Bit IS Planck length.** Size = 1 by definition. Indivisible.
```
bit:      B = 0 | 1           (size = 1)
byte:     D positions: 8      (8 bit positions)
u64:      D positions: 64     (64 bit positions = 8 bytes)
kilobyte: D positions: 1024   (1024 byte positions)
```

**D multiplies L, not B.** Cost = B + D × L
- Topological properties (B) are invariant
- Geometric properties (L) scale with dimension

**We decompose, traverser composes.**
- Express structures as decomposed parts
- Traverser follows paths and composes output

**Lowering IS composition.**
- No separate transformation pass
- Compose with arch-specific structure directly

## Repository Structure

```
bld/
├── src/                    # BLD structures
│   ├── b.bld               # Planck unit (0..1)
│   ├── byte.bld            # 8 bit positions (8*b)
│   ├── traverser/          # HOW to process structure
│   │   ├── x86.bld         # x86 traverser model
│   │   └── x86/            # x86-specific traversal
│   ├── arch/x86/           # x86 instruction encodings
│   │   ├── rex/, modrm/    # Instruction components
│   │   ├── opcode/         # Opcodes by instruction
│   │   └── jcc/, jmp/      # Control flow
│   ├── format/elf/         # ELF64 format
│   ├── program/            # WHAT programs do (structure)
│   │   └── cli/            # CLI algorithm
│   └── os/linux/           # OS-specific structures
├── examples/               # Example structures
└── .claude/skills/bld/     # Claude skill files
```

## The Interpreter

The Python interpreter (`bld-py/`) is bootstrap. It implements:

1. **Parse** - .bld text → structure
2. **Traverse** - Visit B/L/D, compose output

Size comes from D positions. No variables, no emit primitives.

## Remember

> "The structure you find is the structure that exists. BLD doesn't impose—it reveals."
