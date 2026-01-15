# BLD for Software Refactoring

> **Status**: Foundational

## Core Principle

**"Make state explicit"** = align code structure with its inherent BLD.

Refactoring is realignment. The goal isn't to impose structure — it's to reveal the structure that already exists but is hidden.

### Experiential Signals

When reading code, notice your experience:
- **Glide** = structure is explicit, aligned
- **Friction** = hidden state, implicit structure
- **Loops** = circular dependencies
- **Gaps** = hidden L (references you can't see)

**Use friction as a diagnostic signal**: Where you feel friction is where structure is hidden.

The same structures that make code readable also enable:
- Compiler optimization
- CPU branch prediction
- Cache locality
- Parallelization

## Three Patterns

| Pattern | Hidden State | BLD Primitive | Fix |
|---------|--------------|---------------|-----|
| **Dispatch tables** | Implicit state machine | Boundary | Extract to dict |
| **Enumeration** | Invisible state space | Dimension | Config dataclass |
| **DAG dependencies** | Hidden coupling | Link | Break cycles |

## Pattern 1: Dispatch Tables (B)

### Before (Hidden B)
```python
def handle(event):
    if event.type == "click":
        handle_click(event)
    elif event.type == "hover":
        handle_hover(event)
    elif event.type == "scroll":
        handle_scroll(event)
    # ... scattered conditionals
```

### After (Explicit B)
```python
HANDLERS = {
    "click": handle_click,
    "hover": handle_hover,
    "scroll": handle_scroll,
}

def handle(event):
    HANDLERS[event.type](event)
```

**Why it's better**:
- B (event types) is now explicit in HANDLERS keys
- Compiler can optimize dispatch
- Easy to extend (just add to dict)

## Pattern 2: Enumeration (D)

### Before (Hidden D)
```python
def process():
    timeout = 30
    retries = 3
    batch_size = 100
    # ... magic numbers scattered
```

### After (Explicit D)
```python
@dataclass
class Config:
    timeout: int = 30
    retries: int = 3
    batch_size: int = 100

def process(config: Config):
    # D (configuration space) is now explicit
```

**Why it's better**:
- D (parameters) is now a single explicit structure
- Easy to test with different configs
- Clear what can vary

## Pattern 3: DAG Dependencies (L)

### Before (Hidden L)
```python
def compute_result():
    a = fetch_a()      # L1: depends on external
    b = compute_b(a)   # L2: depends on a
    c = compute_c(a)   # L3: depends on a
    d = combine(b, c)  # L4: depends on b, c
    return d
```

### After (Explicit L)
```python
# Dependencies explicit in function signatures
def compute_b(a): ...
def compute_c(a): ...
def combine(b, c): ...

# Or use a DAG framework
dag = DAG()
dag.add_edge("a", "b", compute_b)
dag.add_edge("a", "c", compute_c)
dag.add_edge(["b", "c"], "d", combine)
```

**Why it's better**:
- L (dependencies) is now visible
- Enables parallel execution (b and c can run together)
- Makes testing easier (mock dependencies)

## Performance Connection

| Refactoring | Performance Benefit |
|-------------|---------------------|
| Explicit B (dispatch) | Branch prediction, indirect call elimination |
| Explicit D (config) | Constant propagation, vectorization |
| Explicit L (DAG) | Parallelism, cache locality |

## The Substrate Independence Principle

BLD refactoring works because structure is substrate-independent:

```
Same BLD structure → Same optimization opportunities

Whether the substrate is:
- Python interpreter
- JIT compiler
- GPU shader
- Human reader
```

## Quick Refactoring Guide

1. **Find hidden B**: Look for scattered if/elif chains → extract to dispatch table
2. **Find hidden D**: Look for magic numbers → extract to config dataclass
3. **Find hidden L**: Look for implicit dependencies → make them explicit in types/DAG
4. **Verify**: Does the structure match the domain's natural B/L/D?

## Anti-Patterns

| Anti-Pattern | Problem | BLD Fix |
|--------------|---------|---------|
| God object | Hidden B (modes), hidden L (dependencies) | Split by responsibility |
| Stringly-typed | B encoded in strings | Use enums/types |
| Implicit state | Hidden D (state space) | State machine pattern |
| Circular deps | Tangled L | Break cycles, use events |

---

## The Refactoring Process as Alignment

1. **Read code, notice friction** — Where does processing feel hard?
2. **Interpret the signal** — What's hidden? (B? L? D?)
3. **Apply the pattern** — Extract the hidden structure explicitly
4. **Verify with re-read** — Does it glide now?

When refactoring succeeds, you've aligned code structure with its inherent BLD.
When it doesn't, you've misidentified the hidden structure — try again.

---

## See Also

- [ALIGNMENT.md](ALIGNMENT.md) — Understanding as alignment
- [SKILL.md](SKILL.md) — Main BLD reference
- [Structure as State](../../../docs/theory/structure-as-state.md) — Philosophical foundation
