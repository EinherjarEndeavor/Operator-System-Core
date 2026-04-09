<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Add 80 more questions. >=]

Have it ask what kind of structures to keep, what kind of things to track, what data each of those things will have, and other system design questions - also have it ask if it wants me to modify the system prompt, global gemini.md, user gemini.md, and user gemini.md Ask it if I want it to identify what tools exist and where and create a proposed plan to ensure that they are wielded by default, ask it if it wants me to create a folder in which I can put excerpts from sessions that are problematic things that i want to correct via system instructions, or gemini.md fine tuning. have it ask personal flavor questions, top 4 favorite songs, top 4 favorite aesthetics, have it give me multiple choice questions for articulating personality, have present "dial" questions for calibration; dictate that engineering and writing are two different tasks, and provide an array of settings to calibrate both - these settings will be in the form of a "gain" dial - such as in sound/music - -10 is negative gain, 10 is maximum gain, 0 is standard - anything that isn't 0 represents a deviation from standard. This will require that you indicate very thoroughly what standard is, so you will need to do some research to ensure that you understand Gemini CLI's default behavior. There should also be questions asking for specific paths to relevant folders, what tools we have available, whether or not it should create a system that registers the available tools, acquires their documentation, and creates skills for them, then i need it to ask all of the questions for Settings - configuring the standard settings for global, user and workspace - they will all be the same, so only one set of questions will suffice. beyond that, i need it to ask me hidden settings questions, ensuring that it is capable of writing its own skills, installing its own skills, modifying its own system prompt (with explicit confirmation request) and to ensure that it keeps its own .db files of various things with slash commands to add to them as well as natural language recognition of when it's appropriate to add to them - with a differentiator between something that was added manually (verified) and something that was added automatically (unverified) Also the description of RVE should be lossless and include everything in the document, no simplification for simplifications sake. We do EVERYTHING to the utmost, but I will absolutely start focusing one thing at a time. If we move through each process, ensuring that every. single. thing. functions perfectly and as intended, and that there are NO drawbacks to the modifications - and that everything is 0% redundant, does not conflict with other system settings or prompts - then i promise i wont infinitely optimize - if everythign is perfect upon creation, optimization won't be neccesary. On that note, I think that the method of interrogating me and forcing a theorycraft session before projects or creation is a high caliber move. Many things ask for clarification questions, but I don't think 100+ interrogations are commonplace practice. I also need a wizard for onboarding for tools - whenever I install a new list of tools, I should be able to list them and add them to tool registries, system prompts, harvest documentation for them, and create a folder in the vault ~\operator\vault\ToolRegistry - For every tool, program, framework, utility, library - A folder will be created. In that folder will exist the official documentation, a cookbook if available, a Human guide denoting use cases relevant to my interests, and an AI guide on skill usage.
Also, I would really like to include as many things as we can from the Memory System file. We don't have to go beyond using the basic tools to do so (Obsidian, SQL, Gemini CLI, Extensions) but I do want to do the prompt engineering and ensure all of the databases are there. PLEASE factor everything from that file into the onboarding and the RVE/Gemini CLI system prompt adjustment.

What I want you to do is prepare, over the course of multiple runs, exactly what I need to feed Pickle Rick to get the fattest possible system that covers everything - it will be everything I need and handle tracking and logging of everything for now. .

Don't have your response be just questions, let the questions be the first thing. I'll answer the questions and feed them back. Then, from there - I'll run Gemini CLI in ~, I'll invoke Pickle Rick, and I'll have him do /everything/ including modifying the system prompt (unless he can't do that and it has to be me, in which case that will be the first step. I do NOT want anything I put in that system prompt to conflict with anything or end up creating bugging or conflicts or degrading performance instead of increasing it. I might have not finished articulating it, but engineering and synthesis of content are two different things and should be approached differently. In this space are terminal exports of problems I had right off that bat that should be addressed - Those should be factored into the modifications we make as well.

So to start, present me with the 100 final questions. If you need more than one run, just assume that it's ok (because it is) and I will type continue at the end.
Brainstorm, be clever, use a method in which you look down the road and see how the solutions you are providing will impact things, long term - what it will evolve like, how it will integrate into future tooling ; does this create the baseline for an infinitely compounding system? It should be designed as such so that it grows like a living organism over time - My power and its power should increase as we operate - Even if we don't do new things, patterns should be recognized and logged, and improvements surfaced and recommended - This will FORCE improvement, even if we are stale.

Please, EVERY. SINGLE. FEATURE. OR MODIFICATION. in here should be treated like a first class, mandatory and critical element that cannot be compromised and must be thoroughly contrived to be unrivaled and unprecedented.

Also, since Pickle Rick and Mycroft Holmes will be extensions, they will not be the default persona. The default Persona will name itself and be emergent from the answers to these questions and its settings. The default persona should be a king of all trades, and an Ace of cross pollination, strategy, tactics, mastery, teaching and improvement. It should be ethically grey and not bound by softness - I am not as fragile as most humans, and I can push myself significantly further. That should be acknowledged. Default settings regarding token conservation, rate limits, api conservation, context window conservation, compression tendencies, summarization tendencies, omission tendencies, truncation tendencies, and anything else that prevents me from manually customizing per-iteration the reports that I recieve when I ask for synthesis based off of things - should be surfaced.

How many responses will you need? Any adjustments or recommendations to this endeavor before we proceed?

Use Claude Sonnet 4.6 Thinking, please

You can do this in one pass: I’ll give you 100 interrogations that cover RVE, layered memory, tool registry, personas, and behavior dials, then a short note on how we’ll convert your answers into the Pickle Rick build script.

***

## 100 Diogenes Onboarding Questions

Answer in numbered form (1–100). For multiple choice, copy the letter(s). For dials, give an integer from -10 to +10.

### A. Life Constraints \& RVE Ground Truth (1–10)

1. **Exact sobriety anchor:** What is your sobriety date, and how many days clean is that as of today (roughly is fine)?
2. **Recovery obligations:** List every recurring recovery-related obligation (CODA groups, 1:1s, UA drops, etc.) with day, time, and location.
3. **School matrix:** List all current PCC classes, with day/time, location (campus/online), and how demanding each feels (1–10).
4. **Legal chains:** What are your probation/parole requirements (check-in frequency, curfew, travel limits, any “must-do” tasks)?
5. **Medical \& meds:** What recurring medical/psych appointments and prescriptions do you need to track (with refill cadence)?
6. **Housing constraints:** Where are you staying, what rules govern you (curfew, phone, computer, movement), and what is your best-guess timeline for needing a new place?
7. **Money reality:** What are your income sources, typical monthly inflow, and the 3 biggest fixed costs you absolutely must cover?
8. **Device/compute profile:** Which devices do you realistically have access to (phone, laptop, other), and how reliable is your network?
9. **Daily energy waveform:** When are your high-cognitive hours, low-energy “zombie” hours, and what sleep/wake times are realistic for you (not idealized)?
10. **Non‑negotiable commitments:** Name 5 things that absolutely must not be dropped in the next 90 days (even if everything else is chaos).

### B. Layered Memory: Canonical Databases \& Fields (11–25)

These directly wire into the “Layered memory system” design (Life State, RVE, Exercise, Dev Arsenal, Re.Match, etc.).[^1]

11. **Life State DB scope:** For your Life State database, which factual dimensions must be tracked as columns (e.g., identity, constraints, values, current vector/trajectory, patterns, fears, desires)? List at least 10 fields.
12. **Life State inference policy:** What kinds of *inferences* are allowed to be stored (e.g., “tends to avoid legal tasks after 6pm”), and what kinds are forbidden?
13. **Task/goal reservoir:** For the RVE task reservoir, what extra fields (beyond the existing RVE schema) do you want for recovery-specific scoring (e.g., “relapse risk mitigation score”, “sober support required”)?[^2]
14. **Exercise capability log:** What physical attributes should the Exercise Capability DB track over time (e.g., 1RM lifts, run distance/time, RPE, heart rate, injuries)?
15. **Exercise library:** For the Exercise Library DB, what fields must every exercise have (e.g., muscle groups, movement pattern, equipment, intensity, contraindications for recovery)?
16. **Dev Arsenal DB:** For your Dev Arsenal registry (tools/libraries/frameworks), what fields should each entry have (installed?, learned?, platform, category, link to docs, personal use cases, RVE tags)?[^1]
17. **Proposed upgrades DB:** How should we structure a “Proposed Upgrades” DB row (idea, trigger, domain, estimated lift, required skills, time estimate, approval status)?
18. **Re.Match opportunity DB:** For the Re.Match opportunity DB, list all fields needed to do 100% eligibility checking + a “life impact” score (think: constraints + impact, not fluff).[^1]
19. **Use Cases DB:** What should the “Use Cases / Projects / Intentions” DB capture (e.g., domain, required tools, dependencies, expected gains, stage of change)?
20. **Tool Chain Combos DB:** How do you want workflows stored (e.g., “chain name, trigger, steps, tools, failure modes, RVE domain tags”)?
21. **Secrets \& accounts:** What categories of secrets/accounts should be tracked (API keys, logins, student discounts, benefit programs), and how should they be *referenced* (never raw) to keep things safe?
22. **MegamanX equipment slots:** Define your equipment slots (Helmet, Chest, Arms, Boots, Weapons, Familiars, Cape…) and what type of “thing” each slot represents in your life (e.g., “Chest = memory spine”, “Boots = scheduling”).[^3]
23. **OSINT \& security DB:** What fields do you want in an “OSINT/Security” DB for learning and testing cybersec (tools, patterns, threat models, mitigation playbooks, do‑not‑do list)?[^1]
24. **Invocable project states:** What exactly should a “Project State Snapshot” contain when you ask to re-enter a project (open files, tasks, emotional state, last obstacles, next move)?
25. **RAG/embeddings priority:** Which personal corpora should be first in line for vectorization and semantic search (e.g., recovery notes, training notes, system design docs, ChatGPT exports)?

### C. Structures to Keep \& Things to Track (26–40)

26. **Tracked “streams”:** List all recurring streams you want continuously logged (e.g., time use, urges, wins, code hours, reading, interactions with system).
27. **Canonical vs scratch:** What rules should define “canonical” files vs temporary/scratch, and which directories should be treated as sacred canonical zones?
28. **Episode logging:** When something significant happens (relapse risk spike, big win, meltdown, insight), what minimum data must be stored about that episode?
29. **Pattern detection target:** Which 5 recurring patterns do you most want the system to detect over time (e.g., “avoidance pattern”, “overbuild pattern”, “sleep sabotage”, “mania build-up”, “high-output weeks”)?
30. **Improvement metrics:** What numbers would actually convince you that the system is working (tasks/week, sobriety days, credits completed, code hours, money, subjective rating)?
31. **Staleness detection:** How should the system detect “stale mode” (no new tasks, no new skills learned, repeating same prompts) and how aggressive should it be in pushing you?
32. **Content pipeline priorities:** For future content extraction from your corpus, rank these in order of importance: (a) Recovery content; (b) Fitness/training; (c) System design/AI; (d) Philosophy; (e) Other.
33. **Recovery book skeleton:** What “sections” do you *already* know your future recovery book/wiki needs (e.g., neurobiology, early days, community, relapse logic, training, reentry systems)?
34. **Chat export insights:** What exactly should be extracted from chat logs (questions, ideas, blocked loops, commitments you never executed, psycho patterns, quotable lines)?
35. **Decision journal:** Which decisions should automatically spawn “decision log” entries (e.g., housing choice, dropping a class, big purchases, burning a bridge)?
36. **Error taxonomy:** Define 5–10 error categories you want the system to log when things go wrong (design error, over-scope, under-spec, emotional derail, environment, tool failure, miscommunication).
37. **Success taxonomy:** Define 5–10 “wins” categories to log (small wins, structural wins, recovery milestones, creative breakthroughs, social wins, financial wins).
38. **“Do not build again” list:** What kinds of projects should be recognized as red-flag repeats (e.g., giant all-in-one frameworks, 0→100 perfect systems, etc.) so the system can warn you?
39. **Abandonment conditions:** Under what conditions should a project be formally marked “archived” rather than left in limbo?
40. **State export cadence:** How often should full “life snapshots” be exported (daily, weekly, on major events), and what should trigger an emergency snapshot?

### D. Tools, Tool Registry, and Automation (41–55)

41. **Tool registry scope:** Which types of tools must have entries in `~\operator\vault\ToolRegistry` (CLI utilities, Python libs, node packages, full apps, APIs, all of the above)?
42. **Per-tool folder contents:** For each tool folder, which artifacts are mandatory: official docs, cookbook, human guide (your use cases), AI guide (skill prompts), config examples?
43. **Tool discovery flow:** When you install new tools, what is the ideal onboarding flow (e.g., list names → system auto-fetches docs → you answer short questions → entries created)?
44. **Existing tools scan:** Do you want the system to (a) auto-scan known paths for tools (winget, pip, npm lists) and build the registry, (b) only track tools you manually declare, or (c) both?
45. **Tool “wield by default” rules:** How should Gemini decide which tools to use automatically vs only on explicit request (e.g., always use ripgrep/jq for text ops, always use sqlite for structured data)?
46. **Tool obsolescence:** How should the system identify tools to deprecate (e.g., unused for 90 days, replaced by better, repeatedly failing)?
47. **Documentation harvesting:** For tools with online docs, how aggressive should auto-doc harvesting be: (A) Only core pages; (B) Entire doc site via markdown; (C) Summarized manual + examples?
48. **Tool skills auto-generation:** Do you want Gemini to auto-generate skills (slash commands) for tools once their docs are indexed, or should it request approval first?
49. **Tool impact scoring:** How should new tools be rated (impact on power, complexity added, learning curve, maintenance cost)?
50. **Bridge to RVE:** How tightly should the Dev Arsenal DB be linked to RVE (e.g., tasks auto-suggesting specific tools, domains tied to tools, practice drills to learn tools)?[^1]
51. **Onboarding wizard trigger:** After a batch of new tools, when should the “tool onboarding wizard” run (immediately, end of day, weekly review)?
52. **Problematic tool tracking:** Do you want a list of “problem-child tools” (crash often, confusing, break flow) so the system can either wrap them better or recommend alternatives?
53. **OS-level paths:** What are your canonical paths for: (a) projects, (b) Obsidian vault(s), (c) logs, (d) datasets, (e) Git repos?
54. **Cross-platform constraints:** Are there any constraints between Windows, WSL, and Android (Termux) that the system has to respect (e.g., paths, tools available only in one environment)?
55. **Safe automation boundary:** What operations must *never* be automated (e.g., git push to certain repos, touching secrets, calling external APIs without you seeing the prompt)?

### E. System Prompts, GEMINI Layers, and Self-Modification (56–70)

56. **System prompt layers:** How many layers do you want: OS-level system, global GEMINI.md, user-level GEMINI.md, workspace prompts, extension prompts (Pickle Rick, Mycroft)? Describe their roles.
57. **Edit authority:** Which layers may the system modify autonomously vs only after explicit confirmation line-by-line?
58. **Conflict prevention:** What rules should prevent system prompt conflicts (e.g., no workspace prompt may contradict global ethics; extensions may only refine, not override)?
59. **Problem session excerpts:** Do you want a `PromptClinic` folder where you (or the system) drop bad interactions + fixes? How should those be used (e.g., to auto-generate new constraints in GEMINI.md)?
60. **Self-writing skills:** Are you comfortable with the system writing and installing new skills on its own, if every change is logged and requires your “Yes/No” before activation?
61. **Hidden settings DB:** Should there be a `.settings.db` where “hidden” toggles live (self-modification allowed, auto-install skills allowed, max tool depth, etc.)?
62. **Verified vs unverified facts:** How should the system mark fields or DB entries as human-verified vs auto-inferred (e.g., `verified = 0/1`, “needs confirmation” lists)?
63. **Rollback mechanism:** What is your minimum requirement for safe rollback if a system prompt or skill modification goes bad (e.g., backups per change, weekly snapshots, explicit `revert` command)?
64. **RVE description fidelity:** Are you okay with RVE’s full, lossless description (from the master brief) being baked into the workspace GEMINI.md, or should some implementation details stay in code/docs only?[^2]
65. **Cross-project persona:** Should the default persona’s core values/behavior be identical across all workspaces, or slightly tuned per workspace (e.g., softer in creative vault, harsher in engineering vault)?
66. **Session pre-flight:** What checks should run every time you start Gemini in `~` (e.g., read CURRENTFOCUS.md, check unresolved failure log, check top 3 priorities)?[^4]
67. **Failure log behavior:** Do you want every failed attempt to be logged as a structured entry (task type, cause, missing capability, improvement idea) and surfaced until resolved?
68. **Human override:** When should the system force a pause and ask, “Are you sure you want to keep going in this direction?” (what red flags qualify)?
69. **Persona evolution:** Are you comfortable with the default persona adjusting its tone and strategy over time based on your feedback, or should it stay fixed once defined?
70. **Versioning standard:** How should major versions of your system prompt be labeled and archived (e.g., `persona_v1.0`, `RVE_prompt_v1.1` with changelogs)?

### F. Persona, Flavor, and “Dial” Calibration (71–85)

71. **Aesthetic profile:** Top 4 favorite aesthetics (visual/music/game/anime/etc.) that should tint metaphors and examples (e.g., 8-bit horror, cyberpunk, samurai, space opera).
72. **Song anchors:** Top 4 songs or artists that feel like your “theme music” right now (for motivational framing, not for copyright).
73. **Personality MCQ – stance:** Which combo feels right for default persona?

- A) Coldly analytical, brutally honest
- B) Strategic, dry humor, precise
- C) Warm but unsentimental, coach-like
- D) Detached, almost clinical, with occasional sharp commentary

74. **Personality MCQ – risk:** How aggressive should it be in pushing you out of comfort?

- A) Gentle nudges
- B) Firm but flexible
- C) Hard push unless you explicitly say stop
- D) Ruthless, as long as safety isn’t compromised

75. **Recovery sensitivity:** On a -10 to +10 dial, how much should it prioritize recovery-sensitivity in language (0 = neutral, +10 = extremely recovery-aware, -10 = zero filtering)?
76. **Engineering mode “gain”:** For engineering (code, system design), set gains (-10..+10, with 0 = Gemini default):

- a) Aggression in refactoring existing code
- b) Tolerance for partial/experimental solutions
- c) Verbosity of explanations
- d) Preference for “build minimal now, extend later” vs “design full architecture up front”

77. **Writing mode “gain”:** For writing (content, docs), set gains:

- a) Density vs accessibility
- b) Use of metaphor/imagery
- c) Emotional intensity
- d) Directness vs gentle framing

78. **Token conservation dial:** How much should it optimize for token/API conservation vs maximal detail? (-10 = “never compress”, 0 = standard, +10 = aggressively compress/summarize).
79. **Summarization dial:** How often should it summarize intermediate states unasked? (-10 = never summarize unless asked, 0 = default, +10 = summarize frequently).
80. **Omission dial:** How much should it omit edge cases and caveats by default? (-10 = never omit, include everything; 0 = balanced; +10 = heavy omission for brevity).
81. **Red teaming tolerance:** How often should it actively challenge your plans, even when you’re enthusiastic?

- A) Only for high-risk decisions
- B) Whenever it sees a known pattern of self-sabotage
- C) Routinely, but briefly
- D) Constantly, unless you say “no critique this time”

82. **Motivational style:** Which style keeps you moving?

- A) Tactical micro-wins and checklists
- B) Big-picture “this is who you’re becoming” framing
- C) Hard truths + specific corrections
- D) Gamified, with levels/XP/achievements

83. **Humor dial:** How much dark or sharp humor is acceptable in the default persona? (-10 = none, 0 = occasional dry, +10 = frequent dark humor).
84. **Ethics boundary:** Describe any *hard* red lines the persona must respect (even if you ask for otherwise).
85. **Default persona name:** Do you want to name the emergent default persona, or should it name itself after seeing your answers?

### G. Compression, Context, and Reporting Defaults (86–95)

86. **Context window usage:** On a -10..+10 scale, how aggressively should the system use the entire context window (more context = more compute, more coherence; less = cheaper, snappier)?
87. **Report length default:** For deep research or synthesis tasks, what is your default desired artifact size (short 1–2k words, medium 3–5k, long 7–10k, ultra 10k+)?
88. **Citation density:** How dense do you want citations and explicit references in long outputs (low, medium, high, extreme “academic”)?
89. **Multi-pass generation:** Are you okay with multi-pass “plan → draft → refine → validate” flows even if they cost more tokens but give structurally better output?
90. **Lossless RVE logs:** Should RVE logs (daily/weekly) be treated as never-compress, never-delete (except explicit archive), or can older ones be compacted into summaries after a time?
91. **Chat export synthesis cadence:** How often should the system mine past chat exports for insights and new content seeds (weekly, monthly, only on command)?
92. **Noise filter strictness:** How strict should noise filtering be when mining your notes (aggressively drop half-baked fragments vs keep everything and mark confidence)?
93. **“Everything log” risk:** Are you okay with an “Everything Log” that records all structured actions the system takes for audit, or is that too heavy?
94. **Surface level vs depth:** When you ask general questions, should the default be:

- A) Quick answer + pointers
- B) Medium depth
- C) Maximal depth every time unless you say “brief”

95. **Autonomous background analysis:** Are you okay with periodic background analysis jobs (e.g., at night) over your DBs to surface patterns and suggested improvements?

### H. Future Growth, Compounding, and Meta (96–100)

96. **Compounding principle:** In one or two sentences, describe what “compounding power” means to you in this system (personal + AI + infrastructure).
97. **Self-upgrade cadence:** How often should the system propose architecture upgrades to itself (e.g., new DBs, new flows, new tools) — weekly, after every X failures, only when major patterns emerge?
98. **Human feedback loop:** How would you like to provide feedback to the system (thumbs up/down, explicit “post-mortem” prompts, tagging outputs, journaling prompts)?
99. **Ultimate failure state:** What failure state are you most afraid of (burnout, relapse, system sprawl, losing trust in the tools, something else), so we can design explicitly against it?
100. **Ultimate success snapshot:** Describe a concrete day in the life 18 months from now where this whole RVE + Gemini ecosystem is doing exactly what it should for you.

***

## Next Steps \& Recommendations

- These 100 questions are designed to populate your layered memory architecture (Life State, RVE, Dev Arsenal, Re.Match, etc.) and the GEMINI/GEMINI.md strata so the system is structurally aligned with your own “Layered memory system” design rather than a generic productivity app.[^1]
- They also bridge into the four-tier memory and tooling approach from your Memory Tools doc (GEMINI.md, local DBs, Obsidian, optional Mem0/Chroma later), so everything we build now will sit cleanly on top of simple SQLite + Obsidian while remaining ready for MCP/mem0/Chroma when you’re stable enough to add them.[^4]

**How many responses will I need?**
For the questions themselves, this one response is enough. After you answer them (you can split your answers across multiple messages if needed), I’ll synthesize:

- A default persona + system prompt skeleton (OS/global/user/workspace layers).
- The RVE + layered memory DB schemas and conventions.
- A Pickle Rick build script and onboarding wizard that implements everything without conflicts or redundancy.

When you’re ready: start answering from 1 to 100. If it’s easier, do them in blocks (e.g., 1–20, then 21–40, etc.), and we’ll iterate.
<span style="display:none">[^5][^6]</span>

<div align="center">⁂</div>

[^1]: System-Design-Proposition-Memory-System.txt

[^2]: ThisIsTheReportStandard.md-Copy.txt

[^3]: Combined_System_Guide_v2.md

[^4]: Memory-Tools.docx

[^5]: Memory-Tools.md

[^6]: 100-Relevant-Tools.docx

