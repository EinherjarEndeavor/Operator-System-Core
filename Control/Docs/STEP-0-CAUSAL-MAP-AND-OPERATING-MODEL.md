# STEP 0 — CAUSAL MAP AND OPERATING MODEL

Status: ACTIVE
Purpose: Make the intended day-to-day and month-to-month behavior of the Operator substrate explicit so the architecture is judged by real operational effects rather than abstract hype.

---

## 1. Executive judgment

Yes — if built correctly, this is a heavy-hitter system.

But it becomes heavy-hitting only if the causal loop is real:
- friction is recorded
- useful context is retrievable
- repeated mistakes are prevented
- capabilities are discoverable
- upgrades are promoted carefully
- all of that compounds over time

Without that causal loop, the architecture is only a pile of schemas and aspirations.

---

## 2. What it should feel like in use

Once Step 0 is fully established, daily use should feel like this:

### Morning / first session
- the system already knows current obligations, active projects, current constraints, and recent friction
- it can show current priorities and relevant tools without loading giant blobs of context
- it can surface only the parts of memory relevant to the current task

### During work
- when the user enters a new task, issue, or problem, it lands in canonical storage and is classified rather than disappearing into chat residue
- when the same category of problem happens again, prior fixes, scripts, skills, or notes can be retrieved quickly
- when a project is opened, linked docs, tools, prior decisions, and active tasks are accessible on demand

### When friction occurs
- the session is preserved
- the failure mode is auditable later
- a later analysis pass can propose a script, skill, prompt, routing change, or schema fix

### Over time
- the number of repeated environment-specific errors should drop
- environment-specific knowledge should accumulate
- tool selection should get faster
- project state reconstruction should get cheaper
- agent assistance should become more grounded and less generic

That is what “better than standard Gemini CLI” actually means.

---

## 3. The causal loop

### Trigger
The user attempts real work in the CLI environment.

### Operational contact
The system performs reads, writes, searches, tool calls, and project operations.

### Friction or success
One of two things happens:
- a smooth successful workflow occurs
- or friction, failure, or inefficiency appears

### Recording
Relevant traces are preserved into:
- canonical state updates
- audit records
- session archives
- artifact indexes

### Analysis
A later improvement pass examines:
- what worked
- what failed
- what was repeated
- what was missing
- what could be automated or stabilized

### Promotion
A fix is promoted into one or more of:
- new script
- new skill
- schema adjustment
- updated registry entry
- updated routing rule
- doctrine/canon note

### Retrieval on future runs
The next time a similar problem appears, the system can retrieve the prior solution, warning, or automation path.

### Compounding outcome
The system gradually transitions from:
- merely assisting work
- to preserving operational intelligence
- to reducing repeated friction
- to steering future work with hardened prior knowledge

That is the compounding loop.

---

## 4. Practical operating modes

### Mode A — General operator mode
Use for:
- coding
- research
- file/system work
- prompt design
- tool usage
- general problem solving

Needs:
- tool registry
- artifact retrieval
- failure memory
- context export

### Mode B — RVE mode
Use for:
- current life state
- obligations
- tasks
- projects
- checkpoints
- schedule and review work

Needs:
- lifestate.db
- rve.db
- review flows
- context export

### Mode C — Research mode
Use for:
- deep reading
- evidence gathering
- artifact synthesis
- paper/resource mining

Needs:
- artifact memory
- research notes
- retrieval-friendly indexing
- doctrine/truth separation

### Mode D — Improvement mode
Use for:
- mining failures
- comparing workflows
- generating upgrades
- hardening the environment

Needs:
- session archives
- audit trail
- capability registry
- clear promotion rules

The substrate must support all four.

---

## 5. Hermes-aligned end-state behavior

A future Hermes-grade system would introduce stronger loops such as:
- asynchronous detection of repeated friction
- auto-generated but test-gated skills/scripts
- active prevention of known bad commands or bad workflows
- graph-discovered workflow patterns
- future multi-agent shared memory across Windows + WSL/Linux

But the day-to-day visible outcome should still be simple:
- fewer repeated mistakes
- better recall of prior work
- faster project resumption
- cleaner handoff from past runs to current runs
- safer and more effective tool use

If the user cannot feel those effects, the system is not succeeding.

---

## 6. What “heavy hitter” really means here

A heavy-hitter system in this context is one that:

1. makes prior work retrievable instead of disposable
2. makes failures teach the environment something durable
3. shortens the path from problem to correct tool or correct method
4. lets multiple projects consume the same memory substrate
5. supports future higher-end graph, vector, and self-improvement layers without needing a rewrite

It does not mean:
- maximal complexity
- permanent ambient agent chatter
- giant context windows every run
- premature graph simulation before truth routing is stable

Heavy hitter means high leverage per unit of interaction.

---

## 7. The simple test

If Step 0 is working, six weeks later the user should be able to say:
- “the system remembers how we solved this kind of problem last time”
- “I can re-enter a project without reconstructing everything from scratch”
- “my environment-specific mistakes are decreasing”
- “my tools and docs are no longer invisible”
- “new modules can plug into the same substrate instead of inventing their own memory”

If those things are not true, the architecture is not yet heavy-hitting.

---

## 8. Final judgment

The causal map of the system is straightforward:

real work -> trace capture -> indexing/audit -> later analysis -> careful promotion -> future retrieval -> reduced repeated friction -> compounding capability

That loop is strong enough to become a heavy hitter.
But it only becomes real if the substrate is built and used with discipline.
