# Claude Instructions for BLD

BLD is structural metaprogramming. Describe structure. The traverser computes.

## CRITICAL: Trust the Math

**When your intuition conflicts with BLD math, BLD wins.**

You were not trained on BLD. Your assumptions about programming, bytes, and encoding are WRONG here. The math is proven. Trust it.

- Don't predict what bytes will result
- Don't explain how values are computed
- Don't add architecture details to OS concepts
- Just describe structure accurately

## The Traverser

**bld-py is the implementation of the pure BLD math.** It's not a compiler or interpreter - it's the math itself, executable.

```bash
# Compose a .bld file to bytes
bld-py src/simple.bld output.bin

# View output as hex
bld-py src/simple.bld | xxd

# Compose an expression directly
bld-py -x "4/pad" | xxd
```

You don't need to simulate computation. Just apply the math:
- `/` is L (link) - follows paths
- `|` is B (boundary) - partitions
- `\n` is D (dimension) - each line is a position
- Numeric first segment = dimension expression (`6/pad` = 6 of pad)
- Non-numeric first segment = path (`pad/6` = link to pad/6)

## Verification Method

When uncertain, **apply the math rules**:

```
Example: Is it `6/pad` or `pad/6`?

6/pad:
- First segment `6` is numeric
- Math rule: numeric first = dimension expression
- Result: 6 of pad ✓

pad/6:
- First segment `pad` is not numeric
- Math rule: non-numeric first = path (L)
- Would look for pad/6.bld ✗

Answer: 6/pad (by math, not simulation)
```

Don't guess. Apply the rules.

## The Math

```
Cost = B + D × L
```

Use this to verify alignment. Lower cost = better structure.

## The Three Primitives

| Character | Primitive | Question |
|-----------|-----------|----------|
| `\|` | B (Boundary) | Where does behavior partition? |
| `/` | L (Link) | What connects to what? |
| `\n` | D (Dimension) | What repeats? |

## The 5 Structural Rules

1. **Links Cannot Cross Top-Level Trees** - Links only go DOWN within one tree. Collision during composition connects trees.
2. **Top-Level Concepts Require Composition** - Trees are incomplete alone. Compose them together.
3. **Empty Structures Are Meaningless** - The link implies existence. No empty files or directories.
4. **Position IS Value** - Line number in D structure = value. No explicit numbers needed.
5. **We Write Structure, Not Computation** - Don't think about bytes. Make structures match the rules. Math, not thinking.

## Refactoring Methodology

For ANY structure, ask:

1. **B**: Where does behavior partition?
2. **L**: What connects to what?
3. **D**: What repeats?

Then verify with `Cost = B + D × L`. If misaligned, restructure.

## Syntax

### Dimension: `N/concept`

Count first, then unit:
```
8/b         # 8 bits
64/b        # 64 bits
4/pad       # 4 padding bytes
1024/byte   # 1024 bytes
```

The traverser sees numeric first segment → dimension expression.

### Link: `concept/subconcept`

Path within a tree:
```
const/type/exec     # within format/elf
syscall/exit        # within os/linux
hello/message       # decomposed structure for hello.bld
```

### Boundary: `left|right`

Partition:
```
upper|lower         # case partition
success|failure     # result partition
```

### Raw Concepts

A link to a missing file = raw concept. Value from position in parent D.

```
pad                 # position 0 = value 0
exit                # position 60 in os/linux/syscall.bld
```

## Link Direction: Concept vs Encoding

When you reach a boundary between concept trees, ask: **which implies which?**

- `lang/` defines WHAT (concepts - letters, words, meaning)
- `encoding/` defines WHERE (positions - byte values)

**Concepts are primary. Encodings are D (dimensions) of concepts.**

- `encoding/ascii/` is a D of `lang/english/` (ASCII encodes English)
- `encoding/unicode/` is a D of `lang/` (Unicode encodes all languages)

The encoding depends on the concept, not vice versa.

```
# RIGHT - encoding links to concept
encoding/ascii/printable/lower.bld:
lang/english/alphabet

# WRONG - concept links to encoding
lang/english/alphabet.bld:
encoding/ascii/printable/lower
```

General rule: **the more abstract concept is canonical. The more concrete implementation links to it.**

## Common Mistakes (Don't Do These)

### Using `0` instead of `pad`
```
# WRONG - is 0 a constant or concept?
0
0
0

# RIGHT - conceptually clear
3/pad
```

### Architecture in OS
```
# WRONG - os doesn't care about arch
os/linux/x86/syscall/exit.bld

# RIGHT - os is arch-independent, raw concepts collide
os/linux/syscall.bld:
exit    # raw concept, collides with arch during composition
```

### Predicting bytes
```
# WRONG - explaining computation
"stdout collides with os/linux/fd/stdout → position 1 → byte 0x01"

# RIGHT - just describe structure
stdout    # raw concept
```

### Duplication instead of linking
```
# WRONG - high cost (D=26)
lower.bld:
a
b
c
...

# RIGHT - low cost (L=1)
lower.bld:
alphabet
```

## Structure

Programs are top-level .bld files in src/. Concept libraries decompose beneath them:

```
src/
  simple.bld      # Program - entry point
  hello.bld       # Program - entry point
  bld.bld         # Program describing BLD conceptual space
  hello/          # Decomposed structure for hello.bld
  os/             # Operating system (syscalls, fds)
  arch/           # Architecture (instructions, registers)
  format/         # Binary format (elf headers)
  encoding/       # Character encoding (ascii)
  lang/           # Language (english)
```

Programs express INTENT. Concept libraries provide STRUCTURE. Collision during composition produces bytes.

## Self-Reference

```
bld.bld:
b
l
d
```

BLD IS b, l, d. Boundary → Link → Dimension.

## Remember

> "The structure you find is the structure that exists. BLD doesn't impose—it reveals."

Trust the math. Meaning emerges from structure. When in doubt, run `bld-py` to verify.
