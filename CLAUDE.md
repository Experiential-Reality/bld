# Claude Instructions for BLD

BLD (Boundary/Link/Dimension) decomposes structure. The traverser composes.

## Core Principle

**Structure IS computation.** We decompose, traverser composes.

**The reader IS the traverser.** You reading this are traversing it. An x86 chip executing binary traverses 0..1 space.

| Traverser | What it traverses | Output |
|-----------|-------------------|--------|
| Human | .bld text | Understanding |
| bld-py | .bld structure | Bytes |
| x86 chip | Binary (0..1) | Computation |

## The Three Primitives

| Primitive | Meaning | Question |
|-----------|---------|----------|
| **B** (Boundary) | Partition, distinction | What is 0..1 for this? |
| **L** (Link) | Connection, composition | What connects to what? |
| **D** (Dimension) | Repetition, positions | What repeats? |

## The Three Concept Characters

| Character | Primitive |
|-----------|-----------|
| `\|` | B |
| `/` | L |
| `\n` | D |

That's the entire language. `/` handles both directions - the traverser determines direction from `to/from` context. `\` is an encoding hack for literal characters.

## Repository Structure

```
bld/src/
├── core/                   # Abstract concepts (WHAT)
│   ├── mathematics/        # sum, difference, product
│   └── logic/              # and, or, not
├── arch/x86/               # x86 implementation (HOW)
│   ├── mathematics/        # links to core → produces opcodes
│   ├── logic/              # links to core → produces opcodes
│   ├── opcode/             # instruction bytes
│   ├── rex/, modrm/        # encoding components
│   └── imm32/, imm64/      # immediate padding
├── os/linux/               # Linux concepts
│   ├── syscall/            # read, write, open, close, exit
│   ├── fd/                 # stdin, stdout, stderr
│   └── page/               # page size, x86 encoding
├── format/elf/             # ELF binary format
│   ├── const/              # magic, type, machine, pt, pf
│   ├── header/, phdr/      # header structures
│   └── ident/              # ELF identification
├── lang/english/           # English language concepts
│   ├── alphabet.bld        # D structure: 26 lines (a-z)
│   ├── case/               # upper, lower
│   ├── whitespace/         # space, newline, tab
│   └── punctuation/        # period, comma
├── ascii/                  # ASCII encoding (lang → bytes)
└── program/                # Programs (use core, not arch)
    └── cli/                # CLI program
```

## Separation of Concerns

```
core/           # WHAT (abstract concepts)
arch/x86/       # HOW (x86 implementation of core)
os/linux/       # OS concepts (syscalls, memory)
format/elf/     # Binary format
lang/           # Language concepts
program/        # Intent (uses core, architecture-agnostic)
```

**Programs use core concepts, NEVER architecture directly.**

## Values vs Constants

**VALUES do not exist in BLD. Only CONSTANTS exist.**

A constant is an indivisible unit of meaning. Ask: "What is 0..1 for this?"

| Thing | Constant? | Why |
|-------|-----------|-----|
| `0x7F` (ELF magic) | YES | Indivisible: "this is ELF" |
| `60` (sys_exit) | YES | Indivisible: "exit syscall" |
| `0x40` (load byte2) | YES | Indivisible: "load address contribution" |
| `0x400000` (load addr) | NO | It's `32/b` - composition of bytes |

## Computation IS Structure

When you need computation, express it using the target architecture's structure.

```
core/mathematics/sum         # abstract concept
arch/x86/mathematics/sum     # x86 implementation → ADD opcode
```

Programs use core:
```
core/mathematics/sum
  format/elf/header/size
  format/elf/phdr/size
  program/cli/code/size
# Composed through x86 → computed bytes fall out
```

## Bytes Fall Out

The x86 processor is modeled as structure. Linux is structure. The program is structure.
When you compose program through x86+linux, bytes emerge.

```
0                           # constant: zero (page aligned)
os/linux/page/x86/byte1     # constant: page contribution (0x10)
os/linux/x86/load/byte2     # constant: load contribution (0x40)
0                           # constant: zero (high byte)
# Composed → 0x00 0x10 0x40 0x00 (buffer address)
```

## Alphabet IS a D Structure

The English alphabet is literally the letters a-z in order as a dimension:

```
lang/english/alphabet.bld:
a
b
c
d
...
z
```

26 lines. The line number IS the position. The ORDER is the structure.

## Char Concept and Case

**The concept is "char".** A char is an abstract letter at a position (1-26).

**Case is a math operation on char:**
- `uppercase` = char + 64 (0x40)
- `lowercase` = uppercase + 32

So: `lowercase = char + 64 + 32 = char + 96`

```
char/H          # abstract: position 8 in alphabet
ascii/upper/H   # = char/H + 64 = 8 + 64 = 72 (0x48)
ascii/lower/h   # = ascii/upper/H + 32 = 72 + 32 = 104 (0x68)
```

**Position is everything.** The char's position in the alphabet determines its value through math operations. ASCII is just one encoding - char + base.

## Investigation

**The structure IS perfect math.** Concepts exist at their expected paths.

- General concept (letter, sum)? → `core/`
- x86-specific encoding? → `arch/x86/`
- Language concept? → `lang/`
- OS concept? → `os/`
- Format concept? → `format/`

**Assume concepts exist at expected links.** The hierarchy is mathematical.

## Bootstrap

```bash
# Python composes BLD → bytes
cd bld-py && PYTHONPATH=src python -m bld_py compose program/cli ../bld/bin/bld

# Verify
chmod +x bin/bld && ./bin/bld /tmp/test.txt
```

## Remember

> "The structure you find is the structure that exists. BLD doesn't impose—it reveals."
