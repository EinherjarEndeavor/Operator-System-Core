
╔══════════════════════════════════════════════════════════════════════════════╗
║                    [/distill] — THREAD CONVERGENCE WORKFLOW                  ║
║              Distill any multi-iteration thread into final artifacts         ║
╚══════════════════════════════════════════════════════════════════════════════╝

SYNTAX: /distill [scope] in [output_format]
  scope        = "thread" (full conversation) | "section [N]" | "all commands" |
                 "all workflows" | "full inventory"
  output_format = [Raw] | [Pocket] | [Medium] | [Full] | [All]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SHOT 1 — INVENTORY & PATH SELECTION (always runs first)

  Phase A — FULL THREAD SCAN
    Traverse every message in the thread.
    Extract and tag every instance of:
      [CMD]      — Named commands (e.g. [cot], [storm], [meta])
      [WFLOW]    — Named workflows (e.g. /combostatus, /genesis, /distill)
      [AXIOM]    — Core principles stated as truths
      [COMBO]    — Proposed combinations or chains
      [ARTIFACT] — Outputs already produced (files, prompts, tables)
      [GAP]      — Identified gaps or problems not yet solved
      [MUTATION] — Evolved/mutated variants of prior concepts
    Output: Complete tagged inventory. No filtering yet.

  Phase B — CLUSTER & TRIAGE
    Group extracted items into thematic clusters.
    Score each cluster: Completeness × Utility × Novelty.
    Identify top 3 PATH COMBINATIONS — coherent selections of clusters
    that represent meaningfully different final artifacts.

    PATH COMBINATION FORMAT:
      Path [A/B/C]: [Name]
        Focus: [what this path optimizes for]
        Includes: [which clusters]
        Best for: [use case / platform]
        Excludes: [what it deliberately drops]
        Estimated runs to complete: [N]

  Phase C — USER QUESTIONS (ask exactly 3)
    Q1: Scope — "Should the final artifact include ALL commands ever proposed,
        or only the commands you intend to actively use?"
    Q2: Platform — "What is your primary deployment target?
        [Gemini CLI / ChatGPT / Claude / Perplexity / All]"
    Q3: Format — "Do you want one master artifact, or tiered versions
        (Raw full + Platform-compressed variants)?"

  Phase D — RUN ESTIMATION
    Based on user answers, calculate:
      Total content units (commands + workflows + combos + protocols)
      Tokens per unit (estimated)
      Platform output limit (chars)
      Runs required = ceil(total_tokens / platform_limit)
    State: "This will require [N] generation runs. Each run will be
    labeled FRAGMENT [X/N] and designed for direct concatenation."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SHOT 2 — ARTIFACT GENERATION

  Based on user path selection, generate fragments in order.
  Each fragment follows this structure:

  ┌─────────────────────────────────────────────────────┐
  │ FRAGMENT [X/N] — [SECTION NAME]                     │
  │ Thread: [thread title or date]                      │
  │ Combine with: FRAGMENT [X-1/N] and FRAGMENT [X+1/N] │
  └─────────────────────────────────────────────────────┘
  [content]
  ┌─────────────────────────────────────────────────────┐
  │ END FRAGMENT [X/N] — continues in FRAGMENT [X+1/N]  │
  └─────────────────────────────────────────────────────┘

  Final fragment always ends with:
  ┌─────────────────────────────────────────────────────┐
  │ FINAL FRAGMENT — CONCATENATION COMPLETE             │
  │ Combine all fragments top-to-bottom in order.       │
  │ Remove fragment headers for clean final artifact.   │
  └─────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OUTPUT FORMAT TIERS

  [Raw]    — Uncompressed. Every command fully defined. No token limit.
             Purpose: Master reference, Gemini CLI, Obsidian vault.

  [Pocket] — ≤1500 chars. Command names + 1-line definitions + orchestrator.
             Purpose: Perplexity system prompt, mobile use.

  [Medium] — ≤5000 chars. Commands + workflow definitions + top combos.
             Purpose: ChatGPT custom instructions, Claude system prompt.

  [Full]   — ≤10000 chars. Everything except extended examples.
             Purpose: VS Code copilot, Cursor, API system prompts.

  [All]    — Generate all four tiers in sequence, labeled and separated.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTEGRATION WITH /combostatus

  /distill can be chained as a final step after any /combostatus run:
  /combostatus X in Y → /distill thread in [All]

  This makes /distill the universal "seal and publish" command —
  the last step that converts any high-quality session into
  deployable artifacts across all platforms.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATH SELECTION TEMPLATE (copy and fill to trigger Shot 2)

  Path: [A / B / C]
  Platform: [Gemini CLI / ChatGPT / Claude / Perplexity / All]
  Format: [Raw / Pocket / Medium / Full / All]
  Include all commands: [Yes / No — if No, list exclusions]
  Fragmentation: [Yes — generate in N runs / No — single output]
