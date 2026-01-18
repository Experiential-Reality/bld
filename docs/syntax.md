# BLD Language Syntax

BLD (Boundary/Link/Dimension) expresses structure. The traverser composes.

> For mathematical foundations, see [theory](https://github.com/experiential-reality-org/theory).

## Traversers

| Traverser | Input | Output |
|-----------|-------|--------|
| Human | .bld text | Understanding |
| bld-py | .bld structure | Bytes |
| x86 chip | Binary | Computation |

You reading this are a traverser.

## Constants Not Values

**.bld files contain CONSTANTS and STRUCTURE only.**

Values, state, and accumulation exist in the traverser. The structure is fixed. The traverser moves through it.

## The Three Concept Characters

BLD has exactly THREE concept characters:

| Character | Primitive | Meaning |
|-----------|-----------|---------|
| `\|` | B | Boundary - partitions left from right |
| `/` | L | Link - connects, traversible both directions |
| `\n` | D | Dimension - each line is a position |

That's the entire language.

**`/` handles both directions** - the traverser determines direction from `to/from` context:
- from count → unit = compose (e.g., 8 of b)
- from unit → count = decompose

**Concept characters must be escaped to express the concept as content.**

| Escape | Concept |
|--------|---------|
| `\|` | B (boundary) |
| `\/` | L (link) |
| `\\` | escape itself |

Without escape, `|` IS structure. With escape, `\|` expresses B as content.

`\` is an encoding hack - not a concept, just collision avoidance.

## Self-Reference: bld.bld

BLD defines itself:

```
bld.bld:
b
d
l
```

Three links. BLD IS b, d, l.

## The Three Questions

To describe ANY structure, ask:

| Question | Primitive | What to find |
|----------|-----------|--------------|
| **Where does behavior partition?** | B | Choices, thresholds, type tags |
| **What connects to what?** | L | References, dependencies |
| **What repeats?** | D | Arrays, sequences |

The output is structure. This IS the description.

## The Cost Formula

```
Cost = B + D × L
```

- **B** = boundary cost (topological, invariant under scaling)
- **D** = dimension (repetition count)
- **L** = link cost (geometric, scales with D)

D multiplies L, not B:
- More lines → more link costs
- Boundaries stay local

## Syntax

The filesystem IS the syntax:
- **Files** are concepts
- **Paths** `/` are links (L)
- **Pipes** `|` are boundaries (B)
- **Lines** are dimensions (D)

### Path Resolution

`core/math/add` → `src/core/math/add.bld`

- Paths map to filesystem
- `.bld` extension implicit

## Core Definitions

### b.bld - Boundary

```
0|1
```

Partitions bit-space into two regions.

### l.bld - Link

```
path
```

A reference to another concept.

### d.bld - Dimension

```
d/unit
```

n repetitions of unit. The traverser determines direction from context.

### line.bld - Line Types

```
empty|hex|decimal|field|dimension|path|escaped
```

A boundary partitioning line content types.

### file.bld - File Structure

```
name
d/line
```

A name followed by n lines.

## Boundaries

The pipe `|` partitions space:

```
0|1
empty|hex|decimal|field|dimension|path|escaped
left|right
```

- Left of `|` = one partition
- Right of `|` = another partition (can be link or constant)

## Links

The slash `/` connects:

```
core/mathematics/add
ascii/H
8/b
```

The traverser:
1. Follows the path
2. Composes the target
3. Returns result

Direction determined by `to/from` context.

## Dimensions

Each line is a D position:

```
a
b
c
...
z
```

26 lines = 26 positions. This IS `26/letter`.

Dimension expressions:
- `8/b` = 8 bits (byte)
- `d/line` = n lines (file)
- `64/b` = 64 bits (u64)

## Dispatch Tables

D lines of `constant|link`:

```
classify.bld:
ascii/space|skip
ascii/tab|skip
ascii/newline|next
ascii/hash|comment
```

Structure:
- Each line is a D position
- Each line has `constant|link` (boundary)
- Left of `|` = what to match
- Right of `|` = where to go

## Traversal

The traverser walks structure:

1. **Read** the concept (file)
2. **For each line** (D positions):
   - If `|` present: boundary - match left, follow right
   - Else if `/` present: link - follow path
   - Otherwise: constant - accumulate
3. **Return** accumulated result

**Direction from context**: The traverser knows direction from `to/from` structures, not from the operator.

### Direction Matters

Traversal direction determines operation:
- Forward = one operation
- Reverse = inverse operation

```
core/mathematics/add.bld:
b
b
```

Two operands. Forward = add. Reverse = subtract.

## Composition

When A links to B, B's content composes where the link was:

```
A.bld:        B.bld:        Result:
0x01          0x03          0x01
0x02                        0x02
B                           0x03
```

## The Compensation Principle

L can approximate B, but B cannot approximate L.

- B is topological (local, invariant under D)
- L is geometric (scales with D)
- D×L can approximate complex B
- D×B cannot replace missing L

## Why It Works

BLD = Lie Theory (Sophus Lie, 1870s).

| BLD | Lie Algebra |
|-----|-------------|
| D | Generators |
| L | Structure constants |
| B | Topology |

The cost formula `Cost = B + D×L` IS the Lie algebra dimension formula.

When you decompose into B/L/D, you find the algebraic structure that was always there. The traverser computes the algebra. Bytes fall out.

## Summary

| Character | Primitive | Question |
|-----------|-----------|----------|
| `\|` | B | Where does behavior partition? |
| `/` | L | What connects to what? |
| `\n` | D | What repeats? |

Three characters. Three primitives. The traverser composes.

```
Cost = B + D × L
```
