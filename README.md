# BLD

**Structural metaprogramming.** BLD = Lie theory = Quantum mechanics.

When you write `.bld`, you describe structure. The traverser computes.

---

## The Three Primitives

| Character | Primitive | Question |
|-----------|-----------|----------|
| `\|` | B (Boundary) | Where does behavior partition? |
| `/` | L (Link) | What connects to what? |
| `\n` | D (Dimension) | What repeats? |

That's the entire language.

```
Cost = B + D × L
```

---

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

---

## Top-Level Concepts

```
os/           # Operating system (linux)
arch/         # Architecture (x86)
format/       # Binary format (elf)
encoding/     # Character encoding (ascii)
lang/         # Language (english)
program/      # Programs (intent only)
```

Programs express INTENT. Machines provide IMPLEMENTATION. Composition through collision produces bytes.

---

## Syntax

### Dimension (D) - Newlines

Each line is a position. Line number = value.

```
os/linux/syscall.bld:
read           # position 0 = syscall 0
write          # position 1 = syscall 1
open           # position 2 = syscall 2
...
exit           # position 60 = syscall 60
```

### Link (L) - Paths

Links connect within a tree using `/`:

```
program/hello.bld:
hello/output
exit
```

Raw concepts (no file) get their value from position in parent D.

### Boundary (B) - Partition

The pipe `|` partitions:

```
open|error/open
```

Left = match (success), Right = dispatch (failure).

---

## Examples

### Self-Reference: bld.bld

```
b
d
l
```

BLD IS b, d, l. Three concepts. That's it.

### Simple Program

```
program/simple.bld:
header
phdr
exit
```

Raw concepts that collide during composition with `format/elf`, `os/linux`.

### Hello World Message

```
program/hello/message.bld:
H
e
l
l
o
,

B
L
D
!
lf
```

Each character is a raw concept. Collides with `encoding/ascii` during composition.

---

## The Traverser (bld-py)

bld-py IS the machine. It executes .bld files directly.

### Building a Program

```bash
cd bld-py/src/bld_py
python compose.py "program/simple" > /tmp/simple
chmod +x /tmp/simple
/tmp/simple
echo $?  # exit code 0
```

### Composition

When you compose, top-level trees collide:

```bash
python compose.py "program/simple"
```

The traverser:
1. Resolves links to files
2. Handles dimensions (each line)
3. Handles boundaries (match left, follow right)
4. Raw concepts collide with machine descriptions

Bytes fall out.

---

## The Math

```
Cost = B + D × L
```

| BLD | Lie Algebra |
|-----|-------------|
| D | Generators |
| L | Structure constants |
| B | Topology |

The cost formula IS the Lie algebra dimension formula. When you decompose into B/L/D, you find the algebraic structure that was always there.

---

## Related

- [bld-py](https://github.com/experiential-reality-org/bld-py) - Python traverser (bootstrap)
- [theory](https://github.com/experiential-reality-org/theory) - Mathematical foundations

---

## License

MIT
