# FAILURE MODE GUARDRAILS

Status: Proposed control document
Purpose: Convert repeated failure analysis into explicit rules for generation, ingestion, and architecture work.

## Source basis
This document is derived from the repo's existing failure-analysis and high-volume-generation doctrine.

## Core pattern
The system's recurring failures do not come from lack of intelligence.
They come from:
- semantic compression under pressure
- overwriting instead of preserving deltas
- treating synthesis as distillation
- trying to solve infrastructure limits with prompt intensity alone
- overbuilding before truth and tasks are stable

## Guardrail set A — Anti-truncation

1. Do not ask the chat window to be the factory for 100KB+ outputs.
2. For large artifacts, generate to files in sections.
3. If a document target exceeds safe single-turn output, switch to plan-then-write orchestration.
4. Validate output volume with artifact structure and section completeness, not just rhetorical confidence.
5. Never report success for a long artifact if the output is obviously just a compressed index or vapor summary.

## Guardrail set B — Anti-slop

1. Chain of Density is not permission to delete source-critical detail.
2. Density must increase information per sentence, not reduce evidence surface.
3. If the result becomes more abstract while less operational, the pass failed.
4. Summaries are not doctrine unless explicitly requested.
5. Preserve the ore before refining the ore.

## Guardrail set C — Anti-overwrite

1. Default to append, delta, or versioned output.
2. Never silently overwrite a file in multi-pass generation.
3. If a later pass changes earlier conclusions, preserve a changelog or delta note.
4. The file should show proof of work, not only the latest compressed state.

## Guardrail set D — Anti-canon-corruption

1. Direct facts only enter structured truth by default.
2. Inferred interpretations must be marked provisional.
3. Persuasive artifacts stay artifact-first.
4. Self-issued claims must be tagged as self-issued.
5. Conflicting sources must not be flattened into one fake certainty.
6. Direct user clarification can supersede stale file content, but that override should be visible in provenance.

## Guardrail set E — Anti-architecture-sprawl

1. Do not add new layers because they sound powerful.
2. A new layer must solve a current bottleneck that simpler layers cannot solve.
3. Layer 3 / graph / advanced retrieval remains deferred until Layers 0, 1, 2, and 4 are stable.
4. The current phase succeeds by stabilizing truth, tasks, workflows, and artifacts.
5. Re-design loops are a failure mode, not a sign of sophistication.

## Guardrail set F — Long-form generation policy

1. Plan first.
2. Section second.
3. Generate in chunks with continuity state.
4. Preserve provenance where factual density matters.
5. Run a contradiction and completeness pass before calling the artifact finished.

## Guardrail set G — Ingestion policy

1. Every write must know its target layer before insertion.
2. Every row must have provenance strong enough to explain why it exists.
3. Any row that would be embarrassing to discover was guessed must not be canonical.
4. If a value is gamified, synthetic, or heuristic, keep it out of ground truth unless explicitly marked.
5. Selective ingestion beats heroic bulk ingestion.

## Immediate operator conclusion

When stuck, choose the smaller trustworthy move:
- route truth cleanly
- preserve artifacts separately
- ingest tasks cleanly
- stop adding machinery until the current machinery is trustworthy
