# BLD

**Structural metaprogramming.** Describe structure. The traverser computes.

---

## The Three Primitives

| Character | Primitive | Question |
|-----------|-----------|----------|
| `\|` | B (Boundary) | Where does behavior partition? |
| `/` | L (Link) | What connects to what? |
| `\n` | D (Dimension) | What repeats? |

```
Cost = B + D × L
```

---

## The 5 Structural Rules

1. **Links Cannot Cross Top-Level Trees** - Links only go DOWN within one tree. Collision during composition connects trees.
2. **Top-Level Concepts Require Composition** - Trees are incomplete alone. Compose them together.
3. **Empty Structures Are Meaningless** - The link implies existence.
4. **Position IS Value** - Line number = value.
5. **We Write Structure, Not Computation** - Don't think about bytes. Make structures match the rules. Math, not thinking.

---

## Syntax

### Dimension: `N/concept`
```
8/b         # 8 bits
4/pad       # 4 padding bytes
```

### Link: `concept/subconcept`
```
const/type/exec
hello/message
```

### Boundary: `left|right`
```
upper|lower
```

### Raw Concepts
```
pad         # position 0 = value 0
exit        # position 60 in syscall.bld
```

---

## Self-Reference

```
bld.bld:
b
l
d
```

BLD IS b, l, d. Boundary → Link → Dimension.

---

## Usage

```bash
cd bld-py/src/bld_py
python compose.py "program/simple" > /tmp/simple
chmod +x /tmp/simple
/tmp/simple
```

---

## Methodology

For any structure, ask:

1. **B**: Where does behavior partition?
2. **L**: What connects to what?
3. **D**: What repeats?

Verify with `Cost = B + D × L`. Minimize cost.

---

## Related

- [bld-py](https://github.com/experiential-reality-org/bld-py) - Python traverser
- [theory](https://github.com/experiential-reality-org/theory) - Mathematical foundations

---

## License

MIT
