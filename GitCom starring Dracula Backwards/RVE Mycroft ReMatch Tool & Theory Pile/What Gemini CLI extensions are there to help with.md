<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# What Gemini CLI extensions are there to help with context, memory, and agentic memory sharing - and deep research/research empowerment? Or writing long form

Here's a breakdown of the most relevant Gemini CLI extensions and built-in capabilities across your three focus areas: memory/context, deep research, and long-form writing.

***

## Built-In Memory System

Before any extensions, Gemini CLI has a native `/memory` system worth mastering.  The commands are:[^1_5]

- `/memory add "<text>"` — Appends a persistent fact to `~/.gemini/GEMINI.md` (global) or a project-level `GEMINI.md`
- `/memory show` — Displays all currently loaded context/memory
- `/memory refresh` — Reloads from disk (useful for multi-agent or collaborative setups)

Once saved, facts are silently injected into every future session — the agent "just knows" them without you re-stating them. This is ideal for your workflow: save your writing style, project rules, key decisions, and preferences once and they persist indefinitely.[^1_6]

***

## Context \& Agentic Memory Extensions

**Contextium** is the most powerful option here. It transforms `GEMINI.md` into a *context router* — a dynamic dispatch table that loads only relevant context for your current task. Instead of bloating a single memory file, it gives Gemini access to:[^1_9]

- Project structure, past decisions, historical research
- API/service documentation
- Domain knowledge that's organized and searchable
- Your communication style and preferences

It also features a **multi-agent delegation architecture** — routing tasks to Gemini for research/summarization, Claude for strategy/architecture, and Codex for bulk code generation. Install:[^1_9]

```
# Check: https://github.com/contextium (from Reddit post March 2026)
```

**Neo4j Memory MCP Extension** takes this further with a full knowledge graph backend. The `mcp-neo4j-memory` server persists facts inside Neo4j, allowing agentic flows and Gemini sessions to *recall, update, or forget* stored information — enabling rich, stateful multi-session context that scales far beyond flat markdown files.[^1_4]

***

## Deep Research Extensions

**gemini-cli-deep-research** by Allen Hutchison is the go-to extension here. It wraps Gemini's Deep Research agent (runs on Gemini 3.0 Pro) into MCP, integrating directly with the CLI. It supports two workflows:[^1_7]

1. **Single-question deep investigation** — kick off a focused research task from the terminal
2. **Multi-step iterative research** — structured workflows for complex, layered topics

Install with:

```bash
gemini extensions install https://github.com/allenhutchison/gemini-cli-deep-research --auto-update
```

It requires a `GEMINI_DEEP_RESEARCH_API_KEY` and is billed by token consumption. One noted power move: run research, export outputs as Markdown locally, then continue refining with the CLI — since the CLI handles Markdown far better than Gemini web or Google Docs.[^1_15][^1_7]

***

## Long-Form Writing \& Workflow Extensions

**Conductor** (`@gemini-cli-extensions/conductor`) is the strongest option for structured, long-form output. It's designed to *specify, plan, and implement* features (originally for software), but the planning/implementation pipeline maps well to long-form writing projects — outlines → drafts → revisions.[^1_1]

```bash
gemini extensions install https://github.com/gemini-cli-extensions/conductor
```

**gemini-cli-prompt-library** (`@harish-garg/gemini-cli-prompt-library`) gives you a curated library of battle-tested prompt templates. For writing, this means you can build and store complex prompt chains — intros, section expansions, transitions, editing passes — as reusable slash commands rather than rewriting them every session.[^1_1]

```bash
gemini extensions install https://github.com/harish-garg/gemini-cli-prompt-library
```


***

## Obsidian Integration Bonus

Given your Obsidian usage — the **Agent Client** Obsidian plugin bridges Gemini CLI directly into your vault. It supports auto-mention mode (injects current note context into every message), MCP tool execution, and keyboard-driven workflows. This creates a tight loop: research in terminal → memory saved → writing continued in Obsidian with live Gemini CLI access.[^1_10]

***

## Quick Reference

| Extension | Use Case | Install Command |
| :-- | :-- | :-- |
| Built-in `/memory` | Persistent facts, session continuity | Native |
| **Contextium** | Dynamic context routing, multi-agent | GitHub (March 2026) |
| **mcp-neo4j-memory** | Graph-based long-term agentic memory | Via Neo4j MCP extension |
| **gemini-cli-deep-research** | Full deep research agent in terminal | `allenhutchison/gemini-cli-deep-research` |
| **Conductor** | Planning + implementing long-form work | `gemini-cli-extensions/conductor` |
| **Prompt Library** | Reusable writing/dev prompt templates | `harish-garg/gemini-cli-prompt-library` |
| **Agent Client (Obsidian)** | Gemini CLI inside your vault | Obsidian plugin marketplace |

The highest-leverage combo for your use case is probably: **Contextium** for session memory + **gemini-cli-deep-research** for sourcing + **Conductor** for structured long-form output — all feeding back into persistent `GEMINI.md` memory so context compounds over time.
<span style="display:none">[^1_11][^1_12][^1_13][^1_14][^1_2][^1_3][^1_8]</span>

<div align="center">⁂</div>

[^1_1]: https://geminicli.com/extensions/

[^1_2]: https://github.com/Piebald-AI/awesome-gemini-cli

[^1_3]: https://geminicliextensions.com/browse

[^1_4]: https://cloud.google.com/blog/topics/developers-practitioners/using-the-neo4j-extension-in-gemini-cli

[^1_5]: https://addyosmani.com/blog/gemini-cli/

[^1_6]: https://geminicli.com/docs/cli/tutorials/memory-management/

[^1_7]: https://allen.hutchison.org/2025/12/20/bringing-deep-research-to-the-terminal/

[^1_8]: https://www.linkedin.com/pulse/beyond-prompt-deep-dive-googles-gemini-cli-extensions-allan-smeyatsky-br5af

[^1_9]: https://www.reddit.com/r/GeminiAI/comments/1rzj2yv/i_built_an_opensource_context_framework_for/

[^1_10]: https://forum.obsidian.md/t/new-plugin-agent-client-bring-claude-code-codex-gemini-cli-inside-obsidian/108448

[^1_11]: https://github.com/allenhutchison/gemini-cli-deep-research/blob/main/GEMINI.md

[^1_12]: https://firebase.google.com/docs/ai-assistance/gcli-extension

[^1_13]: https://www.youtube.com/watch?v=OLTjjuyhDCw

[^1_14]: https://github.com/google-gemini/gemini-cli

[^1_15]: https://www.reddit.com/r/GeminiAI/comments/1pfn0vt/deep_research_in_gemini_cli/

