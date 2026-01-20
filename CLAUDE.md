# Claude Instructions for BLD

BLD is structural metaprogramming. Describe structure. The traverser computes.

## Map to Type Theory

BLD primitives ARE type theory constructors you already know:

| BLD | Type Theory | Operation | You Know This As |
|-----|-------------|-----------|------------------|
| B   | Sum (A + B) | case/inject | Pattern matching on variants |
| L   | Function (A → B) | apply | Function application |
| D   | Product (Πₙ A) | project | Tuple/array indexing |

**These are proven irreducible.** No primitive can be expressed using the other two. This follows from cardinality arguments in type theory. Refactoring terminates at B, L, D because they cannot be further decomposed.

```
Cost = B + D × L
```

Cost is conserved—refactoring makes hidden cost explicit, not smaller.

## The Traverser IS Computation

```
Input D  →  Traverser  →  Output D
(source)                  (bytes)
```

The traverser:
1. Reads positions (D lines = values)
2. Follows links (L = products, compose deeper)
3. Partitions (B = sums, select branches)
4. Accumulates position across connected structures
5. Outputs bytes (accumulated positions become output D)

**bld-py** is the traverser. It IS the math, executable.

```bash
bld-py src/simple.bld output.bin   # Compose to bytes
bld-py src/simple.bld | xxd        # View as hex
bld-py -x "4/pad" | xxd            # Expression directly
```

## Operational Semantics

Given `os/linux/syscall.bld` where `exit` is line 60:

```
Step 1: Enter file           → position = 0
Step 2: D-traverse to line 60 → position = 60
Step 3: `exit` is raw concept → no exit.bld exists
Step 4: Position becomes value → 60
Step 5: Value collides        → consuming structure receives 60
```

**This IS computation.** Position accumulation IS the execution model.

### Accumulation Details

**D (newlines)**: Each line increments position
```
syscall.bld:
read        # position 0
write       # position 1
exit        # position 60
```

**L (links)**: Products compose deeper
```
10/10 = 100    # dimension expression (N × M)
```

**B (boundaries)**: Sums partition
```
5|5 = 10       # sum (forward)
left|right     # select side based on accumulated value
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

When the traverser encounters a raw concept (no file exists), its position becomes its value. This value collides with consuming structures during composition.

```
os/linux/syscall/exit → position 60 → value 60 → collides with arch/x86
```

## Refactoring = Reverse Traversal

```
Forward:  B, L, D  →  Bytes    (compose/synthesize)
Reverse:  Structure →  B, L, D  (decompose/analyze)
```

Same primitives. Opposite direction. Same math.

**Refactoring methodology**: For ANY structure, ask:
1. **B**: Where does behavior partition?
2. **L**: What connects to what?
3. **D**: What repeats?

Verify with `Cost = B + D × L`. If misaligned, restructure.

## The 5 Structural Rules

1. **Links Cannot Cross Top-Level Trees** - Collision connects trees
2. **Top-Level Concepts Require Composition** - Trees are incomplete alone
3. **Empty Structures Are Meaningless** - The link implies existence
4. **Position IS Value** - Line number = value (accumulation)
5. **We Write Structure, Not Computation** - Traverser computes, we describe

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

When your intuition conflicts with BLD, BLD wins. The type theory is proven. The math is correct.

- Don't predict bytes
- Don't explain computation
- Just describe structure accurately

The structure you describe IS the computation.
