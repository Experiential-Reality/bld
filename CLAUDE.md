# Claude Instructions for BLD

BLD is structural metaprogramming. Describe structure. The traverser computes.

## Definitions

**Position**: Location in a structure. Line number in a file. Position 0 is first line.

**Value**: A number. In BLD, position IS value - line 5 has value 5.

**D (Dimension)**: Newlines. Each line is a position. D provides constants.
- Syntax: `\n` (implicit), `N/concept` (count × unit)
- Type theory: Product (Πₙ A) - tuple/array indexing

**L (Link)**: Slash. Reference to another structure. L provides indirection.
- Syntax: `concept/subconcept`
- Type theory: Function (A → B) - function application

**B (Boundary)**: Pipe. Partition between alternatives. B provides choice.
- Syntax: `left|right`
- Type theory: Sum (A + B) - pattern matching on variants

**Raw Concept**: Link with no target file. Value comes from position in parent D.

**Accumulator**: Running total. Starts at 0. D increments, L multiplies, B sums.

**Traverser**: Walks structure, accumulates position, outputs bytes. A catamorphism.

**Collision**: When raw concept's value meets consuming structure during composition.

## Why These Three

| BLD | Type Theory | Operation |
|-----|-------------|-----------|
| B   | Sum (A + B) | case/inject |
| L   | Function (A → B) | apply |
| D   | Product (Πₙ A) | project |

**Proven irreducible.** None can express the others. Refactoring terminates at B, L, D.

```
Cost = B + D × L
```

Cost is conserved—refactoring makes hidden cost explicit, not smaller.

## The Traverser IS Computation

```
Input D  →  Traverser  →  Output D
(source)                  (bytes)
```

1. Enters structure (accumulator = 0)
2. Reads D positions (each line increments accumulator)
3. Follows L links (recurse into result)
4. Respects B boundaries (select branch based on accumulator)
5. Raw concept → position becomes value
6. Value collides with consuming structure
7. Output D receives accumulated bytes

**bld-py** is the traverser. It IS the math, executable.

```bash
bld-py src/simple.bld output.bin   # Compose to bytes
bld-py src/simple.bld | xxd        # View as hex
bld-py -x "4/pad" | xxd            # Expression directly
```

## Operational Semantics

Given `os/linux/syscall.bld` where `exit` is line 60:

```
Step 1: Enter file           → accumulator = 0
Step 2: Traverse D to line 60 → accumulator = 60
Step 3: `exit` is raw concept → no exit.bld exists
Step 4: Position becomes value → 60
Step 5: Value collides        → consuming structure receives 60
```

### Link Resolution

Links resolve going UP from current location:
```
At /foo/bar, reference `baz`:
  1. Try /foo/bar/baz   ← start local
  2. Try /foo/baz       ← go up
  3. Try /baz           ← root level
```

Same concept, different resolution point, different value:
```
format/elf/pad.bld → 0 (null byte)
arch/x86/pad.bld   → 144 (NOP)
```

### Collision

**Links only go DOWN within one tree.** Collision connects trees.

```
os/linux/syscall/exit → position 60 → value 60 → collides with arch/x86
```

## Refactoring = Reverse Traversal

```
Forward:  B, L, D  →  Bytes    (compose/synthesize)
Reverse:  Structure →  B, L, D  (decompose/analyze)
```

For ANY structure, ask:
1. **B**: Where does behavior partition?
2. **L**: What connects to what?
3. **D**: What repeats?

Verify with `Cost = B + D × L`. If misaligned, restructure.

## Structural Rules

1. **Links resolve upward** - Local first, then parent
2. **Links cannot cross top-level trees** - Collision connects trees
3. **Position IS value** - Line number = value
4. **Raw concepts get value from position** - No file → value from parent D
5. **We write structure, not computation** - Traverser computes

## Syntax

**Dimension**: `N/concept` (count first, then unit)
```
8/b         # 8 bits
4/pad       # 4 padding bytes
```

**Link**: `concept/subconcept` (path within tree)
```
const/type/exec
syscall/exit
```

**Boundary**: `left|right` (partition)
```
upper|lower
success|failure
```

**Raw Concept**: link to missing file, value from position in parent D

## File Placement

1. **Search** - Does concept exist? `glob src/**/concept.bld`
2. **Think** - What IS this concept? (os? arch? format? encoding? lang?)
3. **Walk** - Start at src/, descend into concept trees
4. **Collide** - Find lowest level where multiple trees need it
5. **Create** - That's where it belongs

## Common Mistakes

**Using `0` instead of `pad`**
```
# WRONG          # RIGHT
0                3/pad
0
0
```

**Architecture in OS**
```
# WRONG                              # RIGHT
os/linux/x86/syscall/exit.bld       os/linux/syscall.bld:
                                    exit    # raw, collides with arch
```

**Predicting bytes** - Just describe structure. Traverser computes.

**Duplication instead of linking**
```
# WRONG (D=26)   # RIGHT (L=1)
lower.bld:       lower.bld:
a                alphabet
b
...
```

## Debugging

**Bottom-up, not top-down.**

1. `bld-py -x "5" | xxd` → `05`
2. `bld-py src/format/elf/const/magic.bld | xxd`
3. `bld-py -x "3|5" | xxd` → `05`
4. `bld-py -x "4/pad" | xxd` → `00 00 00 00`
5. Multi-line: each line = position
6. Composed: build up from simple

If wrong, fix structure. Never modify bld-py. **The traverser IS the math.**

## Trust the Math

When your intuition conflicts with BLD, BLD wins. The type theory is proven.

- Don't predict bytes
- Don't explain computation
- Just describe structure accurately

The structure you describe IS the computation.
