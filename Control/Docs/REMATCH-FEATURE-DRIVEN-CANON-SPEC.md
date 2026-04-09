# REMATCH FEATURE-DRIVEN CANON SPEC

Status: Proposed canon spec
Purpose: Convert the Re.Match concept from scattered mission prose into a buildable service definition.

## 1. Product definition

Re.Match is a constraint-based resource and opportunity matching service for justice-involved, recovery, housing-insecure, and otherwise highly constrained people.

It is not generic job search.
It is profile-aware matching plus dossier generation.

## 2. Primary user promise

If a client provides a complete enough profile, Re.Match can return a prioritized dossier of high-fit opportunities, supports, programs, and action steps that match both hard eligibility and real-life circumstance.

## 3. Core product loop

1. intake profile creation
2. profile normalization
3. opportunity database search / matching
4. deduplication and no-redundancy filtering
5. prioritized dossier generation
6. action-plan packaging
7. follow-up updates as circumstances change

## 4. Core features

### Feature 1 — Full-spectrum intake
The intake must capture enough information to fill out or qualify against many different forms and programs.

The profile should include:
- identity / contact basics
- location and transportation
- housing status and housing barriers
- legal and justice-system history where relevant
- recovery / treatment status
- education / employment / goals
- benefits and insurance
- income and financial constraints
- interests, affinities, and growth directions
- deadlines, active applications, and near-term priorities

### Feature 2 — Constraint-aware matching
Matching must account for:
- hard eligibility
- exclusions / disqualifiers
- geography
- timing
- barriers
- likely life impact

### Feature 3 — No-redundancy logic
The system should avoid returning opportunities already pursued, completed, or known unless there is a new reason to revisit them.

### Feature 4 — Dossier output
Output is not just a list.
It is a dossier organized by life category with:
- recommendation name
- why it fits
- eligibility basis
- required next step
- deadlines / prerequisites
- notes and cautions

### Feature 5 — Opportunity knowledge base
The service needs a maintained opportunity database so every case does not require full deep research from scratch.

### Feature 6 — Humanly useful output
The dossier must be understandable by a stressed user with limited time, limited tech fluency, and limited executive bandwidth.

## 5. Non-goals for current phase

Re.Match does not currently need:
- perfect end-to-end automation
- broad autonomous agent swarms
- production-scale client ops stack
- fancy ML matching beyond strong rule-based and AI-assisted reasoning

## 6. Current MVP operational mode

The likely MVP is:
- structured intake form
- manually/AI-assisted profile normalization
- curated opportunity knowledge base
- dossier generation with explicit action steps

This is already enough to create value.

## 7. What must be canonized next

### Intake canon
A definitive intake schema with required and optional fields.

### Opportunity canon
A normalized schema for opportunities and supports.

### Matching canon
Rules for:
- eligibility
- fit ranking
- redundancy checking
- dossier composition

### Output canon
A dossier format that remains consistent across clients.

## 8. Acceptance criteria

Re.Match current phase is successful when:
1. one intake profile can be normalized cleanly
2. one dossier can be generated from that profile using existing opportunity knowledge
3. the dossier is clear, actionable, and non-redundant
4. the service can explain why each recommendation was included

## 9. Red-team warning

Re.Match fails when it becomes:
- a giant social-mission essay with no repeatable workflow
- a database fantasy before intake and dossier formats are stable
- generic search disguised as matching

Re.Match wins when a constrained user receives a materially useful, accurate next-step package that they would not have found alone.
