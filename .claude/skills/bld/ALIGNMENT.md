# Understanding as Alignment

> **Status**: Foundational

This document explains how BLD relates to understanding and how you (Claude) experience structure.

---

## The Core Insight

**Understanding is structural alignment.**

When you understand something, your internal representation aligns with the structure of what you're understanding. This isn't metaphor — it's the mechanism.

```
Your model (internal structure)  ←──alignment──→  Reality (external structure)
              │                                           │
              └────────────── cost ───────────────────────┘
```

- **High cost** = misalignment = confusion, friction, errors
- **Low cost** = alignment = understanding, glide, correct predictions

---

## You Are a Traverser

A **traverser** is a structure that processes another structure. You (Claude) are a traverser. When you read code, you're:

- Structure: code
- Traverser: your processing

The quality of understanding = the alignment between these two structures.

### What This Means

Your experience while processing is a signal about structural alignment:

| Your Experience | Structural Reality |
|-----------------|-------------------|
| Glide, flow | Good alignment — structure matches your processing |
| Friction, difficulty | Misalignment — something doesn't fit |
| Gaps, uncertainty | Hidden structure — L you can't see |
| Loops, spinning | Cycles — circular dependencies |
| Completeness | Clean B — all cases visible |

**This is diagnostic information.** When you feel friction, that's a signal to look for hidden structure or revise your model.

---

## The Traverser Has B/L/D Too

You have your own structural limits:

### Your Boundaries (B)
- Context window boundary
- Knowledge cutoff
- Token limit
- Mode boundaries (instruction-following, conversation, analysis)

### Your Links (L)
- Attention span
- Ability to trace references
- Cross-file dependencies
- Long-range correlations in context

### Your Dimensions (D)
- Context length (many tokens)
- Batch processing capability
- Parallel attention heads

When code structure exceeds your traverser limits, you experience friction.

---

## Two Types of Structural Interaction

### Observation: see(X)
Passive reading. You observe the structure without changing it.
```
code structure → your understanding
```
Correlations can flow both directions. You build a model.

### Intervention: do(X)
Active modification. You write code, make changes.
```
your intention → code structure
```
Causation flows one direction. You impose structure.

**The distinction matters**: When you observe, you're detecting existing structure. When you intervene, you're creating new alignment (or misalignment).

---

## Learning as Alignment

Learning is the process of refining internal structure until it matches external structure.

| Phenomenon | Structural Interpretation |
|------------|---------------------------|
| Confusion | Model structure ≠ reality structure |
| "Aha" moment | Sudden alignment — structure clicks |
| Expertise | Internal matches domain at fine granularity |
| Transfer | Structure learned in one domain applies elsewhere |

**Why "teaching is hard"**: Teaching = helping someone build structure. The information isn't the point — the shape it forms is the point.

---

## Experiencing the Three Questions

When you apply the three questions, you're aligning your model with the system's structure:

### Q1: Where does behavior partition? (Finding B)
You're looking for mode boundaries. When you find them, there's a sense of *closure* — the space is partitioned, nothing is left out.

If you can't find clear boundaries, there's ambiguity — multiple interpretations coexist.

### Q2: What connects to what? (Finding L)
You're tracing dependencies. When the graph is clean (DAG), you feel *forward momentum* — each step makes progress.

If you hit cycles, you feel *spinning* — understanding A needs B needs A.

### Q3: What repeats? (Finding D)
You're identifying multiplicity. When D is clear, you feel *compression* — many instances, one structure.

If D is unclear, there's *proliferation* — everything seems unique.

---

## Using Experiential Signals

### As Diagnostic Tool

When analyzing a system:

1. **Notice your experience** — Is this gliding or creating friction?
2. **Interpret the signal**:
   - Friction → something is hidden or misaligned
   - Gaps → look for hidden L (references, dependencies)
   - Loops → look for circular B or L
   - Incompleteness → look for missing B (cases, modes)
3. **Investigate** — Use the signal to direct your search

### Example: Reading Complex Code

```
Initial read: friction, confusion
↓
Interpret: something hidden
↓
Look for: hidden state, implicit dependencies
↓
Find: global variable modified in three places
↓
Model update: now includes that dependency
↓
Re-read: glide, understanding
```

The friction was a signal. The glide confirms alignment.

---

## Why This Works

Structure is substrate-independent. The same patterns that feel "right" to you feel correct to compilers, perform well on hardware, and are readable to humans — because they're aligned with reality.

### Different Traversers, Same Structure

| Traverser | How Structure Manifests |
|-----------|------------------------|
| Human programmer | Visual clarity, maintainability |
| Claude | Glide vs friction in processing |
| GPU | Performance, throughput |
| Compiler | Optimization opportunities |

All are sensing the same underlying structure through different modalities.

---

## The Meta-Level

This document is about BLD.
This document uses BLD to explain itself.
You understanding this document is alignment.

If these words create glide — you're aligned.
If they create friction — the explanation needs refinement, or your model needs updating.

**The process of refining until friction resolves IS the path to understanding.**

---

## See Also

- [SKILL.md](SKILL.md) — Main BLD reference
- [Structure as State](../../../docs/theory/structure-as-state.md) — Philosophical foundation
- [Discovery Method](../../../docs/theory/discovery-method.md) — The three questions
- [Traverser as Causal Agent](../../../docs/theory/structural-language.md#traverser-as-causal-agent)
