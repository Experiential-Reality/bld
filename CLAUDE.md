# Claude Instructions for BLD

BLD is structural metaprogramming. It IS quantum mechanics. Meaning emerges from structure.

## The Math

```
Cost = B + D × L
```

Use this formula to detect misalignment. If cost doesn't zero out, the structure is wrong.

## The Three Primitives

| Character | Primitive | Question |
|-----------|-----------|----------|
| `\|` | B (Boundary) | Where does behavior partition? |
| `/` | L (Link) | What connects to what? |
| `\n` | D (Dimension) | What repeats? |

That's the entire language.

## Core Principles

### Structure IS Computation

Don't compute structure. Let structure compute. The traverser (bld-py) just follows B/L/D. Bytes fall out.

### Composing Filesystem Structures

When you compose multiple structures (ascii, arch, os, format, lang), where they **collide** they compose together.

```
ascii.bld:
ascii/control    # 32 entries (0x00-0x1F)
ascii/printable  # 95 entries (0x20-0x7E)
del              # 1 entry (0x7F)
```

When composing `ascii/printable/H`:
1. `ascii/printable` comes AFTER `ascii/control` (32 entries)
2. H is at position 40 in printable
3. Total: 32 + 40 = 72 = 0x48

The base offset comes from the SIZE of preceding structures. By accurately describing the machine with BLD, computation falls out.

### Values Don't Exist

**.bld files contain CONSTANTS and STRUCTURE only.**

- `0x7F` = hex constant (byte)
- `0` = NOT a value. It's `b` - position 0, the boundary
- Decimal numbers are POSITIONS in D structures, not literals

### Position IS Value

In a D structure, the line number IS the value:

```
os/linux/syscall.bld:
read      # position 0 = syscall 0
write     # position 1 = syscall 1
...
exit      # position 60 = syscall 60
```

This IS `unistd_64.h` described with BLD.

### Raw Concepts

A link to a missing file = raw concept. Value comes from position in parent D.

```
os/linux/syscall/exit  # no file exists
                       # value = position 60 in os/linux/syscall.bld
```

### Contiguous D vs Dispatch Table

**Contiguous D** (ordered, no gaps): Just concept names. Position IS value.
```
read
write
exit
```

**Dispatch table** (partitioned): `constant|link` format.
```
os/linux/syscall/open|program/cli/error/open
```
Left = match, Right = dispatch. Used for success|failure partitions.

### Links Provide Context

Inside a structure, links to self are redundant:
```
# WRONG - redundant links inside os/linux/syscall.bld
os/linux/syscall/read
os/linux/syscall/write

# RIGHT - just concept names
read
write
```

But links ADD meaning when context matters:
```
# os/linux/fd.bld - links provide fd context
os/linux/fd/stdin
os/linux/fd/stdout
os/linux/fd/stderr
```

## BLD Refactoring Methodology

When you discover friction, don't skip it. Fix it. You can't understand the concept until you do.

For each structure, ask:

1. **B**: Where does behavior partition?
2. **L**: What connects to what?
3. **D**: What repeats?

Then verify with `Cost = B + D × L`. If misaligned, restructure.

## Writing BLD

### DO
- Express intent, not implementation
- Use hex (`0x`) for byte constants
- Use boundaries (`|`) for success|failure partitions
- Trust position - line number IS value
- Let structure compute

### DON'T
- Use decimal literals as values (they're positions)
- Put `0` in files (it's `b`, implicit at position 0)
- Add redundant links inside structures
- Pre-decompose (put arch details in programs)
- Change the traverser math

## Structure Hierarchy

```
core/           # Abstract concepts (WHAT)
arch/x86/       # Architecture encoding (HOW)
os/linux/       # OS concepts (syscalls, fds)
format/elf/     # Binary format
lang/           # Language concepts
program/        # Intent (uses os/core, NOT arch)
```

Programs express intent. Architecture provides encoding. The traverser composes.

## The Conceptual CLI

```
bld <from> <to> <start> <output>
bld bld.bld os/linux,arch/x86,format/elf program/cli bin/
```

- **from**: source format (bld.bld)
- **to**: target formats (os, arch, format)
- **start**: what to compose (program)
- **output**: where to write

## Examples

### Syscall (contiguous D)
```
os/linux/syscall.bld:
read
write
open
close
...
exit
```
Position 60 = exit = syscall 60.

### Boundary (success|failure)
```
program/cli/open.bld:
os/linux/syscall/open|program/cli/error/open
```
Open syscall OR error handler.

### Program (intent only)
```
program/cli/exit.bld:
os/linux/syscall/exit
```
Just the syscall. No `0` needed - boundary is implicit.

## Remember

> "The structure you find is the structure that exists. BLD doesn't impose—it reveals."

Trust the math. Meaning emerges from structure.
