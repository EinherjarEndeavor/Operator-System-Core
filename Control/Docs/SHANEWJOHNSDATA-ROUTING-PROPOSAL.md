# SHANEWJOHNSDATA ROUTING PROPOSAL

Status: Proposed staging document
Purpose: Decide what should be ingested, what should remain artifact-only, and what should be deferred pending user review.

## File-by-file routing

### 1. ShaneJohnsRe.MatchAnswers4.8.26.txt
Role: primary structured source
Recommendation: ingest selectively into Layer 2

Best candidates for Layer 2:
- stable profile fields
- contact fields
- housing and logistics fields
- program / treatment fields
- benefits and eligibility fields
- education and work-history references
- explicit barriers / constraints
- explicit priorities and deadlines

Do not auto-ingest as canon:
- rhetorical mission language
- broad self-description paragraphs
- subjective self-positioning
- conflicting fields without review

Required handling:
- field-by-field parsing
- provenance on every inserted row
- conflict tagging where the file disagrees with other sources

### 2. RESUME (1).html
Role: selective structured source + artifact
Recommendation: split usage

Use for Layer 2 only when extracting:
- employer names
- role names
- year spans
- certifications
- contact info if needed

Keep in Layer 4:
- summary paragraph
- competency phrasing
- disclosure framing
- reference formatting and presentation style

Required handling:
- do not treat resume summary language as literal truth without corroboration

### 3. CERTIFICATE (1).html
Role: milestone artifact with some extractable facts
Recommendation: mostly Layer 4, with selective tagged extraction

Possible Layer 2 candidates:
- externally verifiable milestone statements only
- concrete dated completions if corroborated elsewhere

Keep in Layer 4:
- certificate presentation
- self-certification framing
- status rhetoric

Required handling:
- tag any extracted milestone as self-issued unless independently verified

### 4. COVER_LETTER (1).html
Role: persuasive artifact / voice exemplar
Recommendation: Layer 4 only by default

Possible selective extraction:
- only facts that are corroborated by stronger sources

Do not auto-ingest:
- narrative claims
- persuasive framing
- branding language
- audience-specific positioning

## Recommended current ingestion order

1. ShaneJohnsRe.MatchAnswers4.8.26.txt
2. RESUME (1).html
3. CERTIFICATE (1).html
4. COVER_LETTER (1).html

## Proposed write policy by file

### Primary source policy
Use the structured answer file as the main truth candidate source.

### Secondary corroboration policy
Use resume and certificate only to reinforce or supplement already structured facts.

### Artifact-first policy
Use cover letter and most certificate/resume prose as Layer 4 artifact material, not database truth.

## Required review triggers

Trigger review before writing when:
- a field conflicts with another source
- a statement is prestige-oriented rather than factual
- a statement is self-issued or self-evaluative
- a narrative sentence must be converted into a structured fact
- a missing schema field is required to hold the data

## Practical conclusion

This folder is worth using.
The mistake would be treating all files inside it as equal truth sources.
They are not equal.
The structured answer file is the main Layer 2 candidate.
The other three files are mostly Layer 4 artifacts with selective fact extraction.
