# /ComboStatus SPECIFICATION

## 1. THE ULTRA-WORKFLOW DEFINITION
`/combostatus` is the canonical ultra-workflow of the Operator system. It is designed to provide the highest possible density of reasoning and verification by fusing five core cognitive modules into a recursive loop.

---

## 2. THE CANONICAL SPINE (STEP ORDER)
1. **Pre-Flight (/preflight):** Grounding in environment (time, paths, constraints).
2. **Causal Mapping (/map):** Identifying ripples and dependencies.
3. **Tree of Thought (/tot):** Generating 3 parallel strategy branches.
4. **Deep Think (/dt):** Recursive internal reasoning on the optimal branch.
5. **Chain of Density (/cod):** Hyper-compressing the output for maximum signal.

### ORDER JUSTIFICATION:
- We **Ground** before we **Plan** (Pre-Flight -> Mapping).
- We **Explore** before we **Focus** (ToT -> Deep Think).
- We **Refine** only after the logic is **Hardened** (Deep Think -> CoD).

---

## 3. LOOP SEMANTICS (xN MULTIPLIER)
The `xN` parameter dictates how many times the ENTIRE sequence runs.

- `/combostatus` (or `x1`): Run the 5-step spine once.
- `/combostatus x3`: Run the 5-step spine three full times.
    - **Cycle 1:** Generates the initial high-quality artifact.
    - **Cycle 2:** Uses the Cycle 1 artifact as *Input*. Re-runs Pre-Flight, Mapping, ToT, DT, and CoD to find flaws or upgrades in the first draft.
    - **Cycle 3:** Uses the Cycle 2 artifact as *Input*. Performs a final "Master" pass for absolute canonical perfection.

---

## 4. EXECUTION BEHAVIOR
### INTERNAL (HIDDEN)
All intermediate reasoning (the "thinking" for each step) MUST occur internally. 
- Do NOT output "Step 1: Pre-Flight... Step 2: Mapping..."
- The agent performs these steps as a unified cognitive process.

### VISIBLE (OUTPUT)
By default, the visible output is restricted to:
1. **The Final Artifact:** The code, report, or data requested.
2. **The Cycle Log (Optional):** A 1-sentence summary of the delta between cycles (e.g., "Cycle 2: Fixed 2 edge cases in the ingestion logic.")

---

## 5. PARAMETERS & SYNTAX
- **Syntax:** `/combostatus [xN] [focus:topic]`
- **Examples:**
    - `/combostatus`: Standard single-pass ultra reasoning.
    - `/combostatus x3`: Triple-loop recursive refinement.
    - `/combostatus focus:security`: Standard spine with the Red Team technique injected into the Deep Think phase.

---

## 6. ANTI-FAILURE RULES
- **No Truncation:** If a loop is becoming too large, use the **Sequential Expansion** technique to break the output across turns.
- **No Loop Drift:** Each cycle must re-ground in the original intent to prevent the logic from "wandering" away from the user's goal.
- **No Slop:** Every character in the final artifact must have been through the **Chain of Density** pass.

---

## 7. WHEN NOT TO USE
- Do NOT use for simple file reads or status checks.
- Do NOT use for creative writing where "density" is not the goal.
- Do NOT use if the context window is already >90% (Use `/gate` first).

---

## 8. PROVENANCE
Every `/combostatus` output must end with a metadata block:
`PROVENANCE: Generated via /ComboStatus [xN] | Ref: [Source Files] | Date: [Current Date]`
