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

## The 5 Structural Rules

### Rule 1: Links Cannot Cross Top-Level Trees
Links only go DOWN within a single top-level tree. Cross-concept meaning arises through **collision** during composition.

### Rule 2: Top-Level Concepts Require Composition
Top-level trees are incomplete in isolation. They MUST be composed together. Only BLD primitives (`b.bld`, `d.bld`, `l.bld`, `bld.bld`) stand alone.

### Rule 3: Empty Structures Are Meaningless
Empty directories and empty files encode nothing. Raw concepts are implied by the link itself - if you link to something, it exists.

### Rule 4: Position IS Value
Line number in D structure = value. No explicit numbers needed.

### Rule 5: We Write Structure, Not Computation
The pure traverser IS the machine. Don't change it - change .bld files. **Don't think about bytes - just make structures match the rules. Math, not thinking.**

## Core Principles

### Machine Descriptions

Each top-level directory describes a machine's structure/capabilities:

```
os/linux/         # Linux machine - syscalls, fds, pages
arch/x86/         # x86 chip - instructions, registers, encoding
format/elf/       # ELF format - headers, sections
lang/english/     # English language - letters, punctuation
encoding/ascii/   # ASCII encoding - control, printable
program/          # Programs - intent only
```

Programs express INTENT. Machines provide IMPLEMENTATION. Composition connects them.

### Collision Model

Links CANNOT cross between top-level concepts. Cross-concept meaning arises ONLY through collision.

```
# WRONG - cross-tree linking
program/hello/output.bld:
os/linux/fd/stdout      # links to different tree!

# RIGHT - concepts within own tree
program/hello/output.bld:
stdout                  # raw concept
message                 # link down
write                   # raw concept
```

When composed with `os/linux`:
- `stdout` COLLIDES with `os/linux/fd/stdout` → position 1
- `write` COLLIDES with `os/linux/syscall/write` → position 1

Collision produces meaning. Not explicit links.

### Composing Filesystem Structures

When you compose multiple structures (encoding, arch, os, format, lang), where they **collide** they compose together.

```
encoding/ascii.bld:
control    # 32 entries (0x00-0x1F)
printable  # 95 entries (0x20-0x7E)
del        # 1 entry (0x7F)
```

When composing with `encoding/ascii`:
1. `H` in program collides with `H` in `encoding/ascii/printable`
2. `printable` comes AFTER `control` (32 entries base)
3. H is at position 40 in printable
4. Total: 32 + 40 = 72 = 0x48

The base offset comes from the SIZE of preceding structures. By accurately describing the machine with BLD, computation falls out.

### Values Don't Exist

**.bld files contain CONSTANTS and STRUCTURE only.**

- `0x7F` = hex constant (byte)
- `0` = NOT a value. It's `b` - position 0, the boundary
- Decimal numbers are POSITIONS in D structures, not literals

### Position IS Value (Rule 4)

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
open|error/open
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

Links go DOWN within a tree. Cross-tree meaning comes from collision:
```
# program/hello/output.bld - raw concepts that collide
stdout
message
write
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

**Machine descriptions (require composition):**
```
os/           # Operating system (linux)
arch/         # Architecture (x86)
format/       # Binary format (elf)
encoding/     # Character encoding (ascii)
lang/         # Language (english)
program/      # Programs (intent only)
```

**Pure BLD definitions (standalone):**
```
b.bld         # Boundary: 0|1
d.bld         # Dimension: d/b
l.bld         # Link: path
bld.bld       # Self-reference: b, d, l
```

Programs express intent. Machines provide encoding. Composition through collision produces bytes.

## The Pure Traverser (bld-py)

bld-py IS the machine. It executes .bld files directly - not compilation, direct execution.

```
python compose.py "program/simple"
```

The traverser:
1. Resolves links to files
2. Accumulates constants (hex/decimal bytes)
3. Handles dimensions (each line)
4. Handles boundaries (match left, follow right)

State doesn't exist until traversed - like quantum mechanics, measurement collapses the structure to bytes.

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
open|error/open
```
Match left (success), dispatch right (failure handler).

### Program (intent only)
```
program/exit.bld:
exit
```
Just the raw concept. When composed with `os/linux`, `exit` collides with `os/linux/syscall/exit` → position 60.

## Remember

> "The structure you find is the structure that exists. BLD doesn't impose—it reveals."

Trust the math. Meaning emerges from structure.
