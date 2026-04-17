# STEP 0 — MODULAR CAPABILITY FAMILIES AND TWIN LOOPS

Status: ACTIVE
Purpose: Define how major capability families plug into the Operator substrate and clarify the two optimization loops that the memory architecture must eventually serve.

---

## 1. Executive judgment

The Operator system should not be built as one monolith.
It should be built as a stack of modules with explicit attachment points.

The substrate is the base.
Major capability families plug into it.
Each major family should expose:
- insertion points into the substrate above and below
- clear data contracts
- clear audit surfaces
- clear retrieval surfaces

This allows the system to grow like interlocking parts rather than like one tangled app.

---

## 2. The modular rule

Every major capability family should be treated as a Lego-like module.

That means each family needs:

### Upward interface
What later layers can consume from it.
Examples:
- structured outputs
- summaries
- logs
- metrics
- artifacts
- routed events

### Downward interface
What it requires from the substrate.
Examples:
- canonical state
- tool registry
- audit logging
- artifact indexing
- context exports
- doctrine references

### Sideways interface
How it connects to peer capability families.
Examples:
- browser stack feeding research stack
- research stack feeding RVE or Re.Match
- subjective-memory lane feeding coaching or checkpoint logic
- audit loop feeding system hardening

---

## 3. The twin loops

The long-range memory architecture exists to support two major optimization loops.

### Loop A — System Optimization
Purpose:
Improve the machine.

Inputs:
- session logs
- tool failures
- browser runs
- script outputs
- MCP health
- audit records
- repeated friction
- routing mistakes

Outputs:
- new skills
- better wrappers
- better schemas
- better routing rules
- capability promotion or deprecation
- hardened procedures
- better operator ergonomics

This loop makes the environment itself better.

### Loop B — Shane Optimization
Purpose:
Improve the operator.

Inputs:
- journals
- reflections
- life-state updates
- learning logs
- training notes
- task friction
- opportunity observations
- behavioral patterns
- later physiological inputs if adopted

Outputs:
- pattern summaries
- growth constraints
- skill progression markers
- opportunity vectors
- better routines
- better planning context
- better coaching/review surfaces

This loop makes the human better.

The substrate should eventually support both loops without confusing them.

---

## 4. Why the memory architecture matters most

Memory architecture is the common force multiplier because it determines whether the system can:
- preserve useful state
- distinguish objective truth from subjective signals
- retrieve prior work
- learn from repeated friction
- promote durable improvements
- support future modules without losing coherence

If memory is weak, every capability family becomes shallow.
If memory is strong, each family compounds the others.

---

## 5. Major capability families

The Step 0 substrate should be able to support at least the following capability families over time:

1. acquisition and browser operations
2. research and synthesis
3. structured life/execution systems such as RVE
4. subjective memory and self-observation
5. capability registry / arsenal awareness
6. audit and system hardening
7. future service systems such as Re.Match
8. future learning/tutoring systems

Not all of these need to be fully built now.
But the substrate should not block them.

---

## 6. Immediate design consequence

During Step 0, when a major family is being designed in depth, the correct question is not:
- “is this the whole system?”

The correct question is:
- “what are this family’s attachment points to the substrate and to later modules?”

This keeps the work grounded without forcing the entire future system into the current sprint.

---

## 7. Example: acquisition and browser operations

This family is not the whole system.
But it is a major capability family.

It should plug into the substrate through:
- tool registry
- audit logs
- artifact indexing
- source monitoring
- retrieval and provenance tagging

It should output upward into later layers such as:
- research artifacts
- curated source bundles
- monitored-source updates
- captured pages and summaries
- structured data for future databases

This is why designing it carefully matters without making it the center of gravity.

---

## 8. Final judgment

The Step 0 build should proceed module by module.
Each major family should be designed as a high-quality attachment to the substrate.

The long-range goal is not one huge app.
It is a coherent stack where the substrate supports both:
- system optimization
- Shane optimization

That is the correct frame for continuing the work.
