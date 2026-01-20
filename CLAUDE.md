# Claude Instructions for BLD

BLD is structural metaprogramming. Describe structure. The traverser computes.

## The Traverser IS a Process

```
Input D  →  Traverser  →  Output D
(source)                  (bytes)
```

The traverser transforms one dimension structure into another. It reads BLD source (positions in files), follows structure, and produces bytes (positions in output).

**bld-py** is the traverser. It IS the math, executable.

```bash
bld-py src/simple.bld output.bin   # Compose to bytes
bld-py src/simple.bld | xxd        # View as hex
bld-py -x "4/pad" | xxd            # Expression directly
```

## The Three Primitives

| Character | Primitive | Forward | Reverse |
|-----------|-----------|---------|---------|
| `\|` | B (Boundary) | Sum | Difference |
| `/` | L (Link) | Product | Quotient |
| `\n` | D (Dimension) | Position | Position |

**Traversal is bidirectional.** Forward traversal composes (sum, product). Reverse traversal decomposes (difference, quotient). This enables both encoding and decoding from the same structure.

```
Forward: 5|5 = 10 (sum),    10/10 = 100 (product)
Reverse: 10 → 5 (difference), 100 → 10 (quotient)
```

## Why These Three

B, L, D are **proven irreducible** from type theory:

| Primitive | Type | Property |
|-----------|------|----------|
| B | Sum type | Choice between alternatives |
| L | Function type | Reference/indirection |
| D | Product type | Tuple/repetition |

None can be expressed using the other two. This isn't design—it's mathematics.

**Refactoring IS factorization:**
```
FACTOR : S → S₁ × S₂ × ... × Sₙ
```

Refactoring decomposes composite structures into B, L, D. It terminates at these primitives because they cannot be decomposed further. The three refactoring patterns (extract dispatch table, break cycles, separate loops) are the same insight: find hidden B, L, or D and make it explicit.

```
Cost = B + D × L
```

## Cost Conservation

Cost is **conserved**, not reduced:

```
C_total = C_visible + C_hidden   (always conserved)
```

Refactoring doesn't make structure simpler—it makes **hidden cost explicit**. The goal is explicitness, not minimization.

| Before Refactoring | After Refactoring |
|-------------------|-------------------|
| C_visible: small | C_visible: large |
| C_hidden: large | C_hidden: small |
| C_total: **same** | C_total: **same** |

When you refactor, you're revealing structure that was always there. The cost was being paid implicitly. Now it's auditable.

## The Compensation Principle

**B and L are asymmetric.** The cost formula `B + D × L` reveals this:
- **B is topological** - local, invariant under scaling
- **L is geometric** - scales with distance (multiplied by D)

This creates an asymmetry:

| Direction | Works? | Why |
|-----------|--------|-----|
| L → B | ✓ Yes | Cascading links can approximate boundaries |
| B → L | ✗ No | Boundaries stay local, can't reach distant information |

**Links can compensate for missing boundaries** (through cascading). **Boundaries can never compensate for missing links.** This affects design: when in doubt, add links. You can always partition later.

## Accumulation

The traverser **accumulates position** as it walks structure:

**D (newlines)**: Each line increments position
```
syscall.bld:
read        # position 0
write       # position 1
exit        # position 60
```

**L (links)**: Following a link multiplies through depth
```
10/10 = 100    # dimension expression
N/M = N × M    # numeric first = multiply
```

**B (boundaries)**: Partitions sum or select
```
5|5 = 10       # sum (forward)
left|right     # select side based on accumulated value
```

**Accumulation is multidimensional.** Each connected structure is a dimension. As the traverser follows links, it accumulates relative position in each structure. The output emerges from combining positions across all connected dimensions.

## Link Resolution

**Links are relative to connected structures. Resolution goes UP.**

When the traverser encounters a link, it resolves from the current location upward:

```
At /foo/bar, reference `baz`:
  1. Try /foo/bar/baz   ← start local
  2. Try /foo/baz       ← go up
  3. Try /baz           ← root level
```

The level where the link **resolves** is where **collision** happens. That structural position determines meaning.

```
In format/elf/:   `pad` resolves to format/elf/pad.bld   → 0 (null)
In arch/x86/:     `pad` resolves to arch/x86/pad.bld    → 144 (NOP)
At root level:    `pad` resolves to src/pad.bld         → 0 (default)
```

Same concept, different resolution point, different value. **The structure determines meaning.**

**This is multidimensional accumulation.** As the traverser follows links across connected structures, it accumulates position in each:

```
format/elf/header.bld     → position in format tree
  → links to arch/x86/... → position in arch tree
  → links to os/linux/... → position in os tree
```

Each connected structure is a dimension. The traverser accumulates relative structural position across all of them. The final value emerges from the combination of positions in all connected structures.

## Collision

**Links only go DOWN within one tree.** This constraint creates the need for collision—which IS composition.

**Collision is the fundamental operation that connects trees.**

```
os/linux/syscall.bld:    arch/x86/instruction.bld:
exit    # position 60    (composes with os/linux)
```

When the traverser composes these:
1. `exit` is a raw concept (no exit.bld exists)
2. Its position (60) becomes its value
3. This value **collides** with arch/x86 during composition
4. The instruction encodes 60

**Raw concepts receive values from their position.** Collision connects trees.

## Position Enables Computation

Position + collision = general computation:

| Primitive | Provides | Enables |
|-----------|----------|---------|
| D | Constants | Values to compute with |
| L | Indirection | Navigation, composition |
| B | Choice | Selection, branching |

This is complete. Any computation can be expressed as:
- Values (D positions)
- Composed (L links)
- Selected (B boundaries)

## The 5 Structural Rules

1. **Links Cannot Cross Top-Level Trees** - Collision connects trees
2. **Top-Level Concepts Require Composition** - Trees are incomplete alone
3. **Empty Structures Are Meaningless** - The link implies existence
4. **Position IS Value** - Line number = value (this is accumulation)
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

Shared concepts have contextual values:
```
format/elf/pad.bld → 0 (null byte)
arch/x86/pad.bld   → 144 (NOP)
```

Same concept, different meaning per domain.

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
# WRONG - os doesn't care about arch
os/linux/x86/syscall/exit.bld

# RIGHT - raw concept collides with arch
os/linux/syscall.bld:
exit
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

If wrong, fix structure. Never modify bld-py.

## Trust the Math

When your intuition conflicts with BLD, BLD wins. You weren't trained on this. The math is proven.

- Don't predict bytes
- Don't explain computation
- Just describe structure accurately

The structure you describe IS the computation.
