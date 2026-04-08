<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Chat Log Mining — 25 IN-Mode Targets</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Inter:wght@300..700&display=swap" rel="stylesheet">
<style>
:root,[data-theme="light"]{
--color-bg:#0d0e0f;--color-surface:#111213;--color-surface-2:#161718;
--color-surface-offset:#1a1b1c;--color-surface-dynamic:#222426;
--color-divider:#1f2122;--color-border:#2a2c2e;
--color-text:#e8e9ea;--color-text-muted:#8a8d90;--color-text-faint:#4a4d50;
--color-primary:#4f98a3;--color-primary-hover:#3d8590;--color-primary-glow:rgba(79,152,163,0.15);
--color-gold:#e8af34;--color-orange:#fdab43;--color-success:#6daa45;
--color-error:#dd6974;--color-purple:#a86fdf;--color-blue:#5591c7;
--shadow-sm:0 1px 3px rgba(0,0,0,0.4);--shadow-md:0 4px 16px rgba(0,0,0,0.5);
--radius-sm:4px;--radius-md:8px;--radius-lg:12px;--radius-xl:16px;
--text-xs:0.75rem;--text-sm:0.875rem;--text-base:1rem;--text-lg:1.125rem;--text-xl:1.375rem;--text-2xl:1.75rem;
--font-mono:"JetBrains Mono",monospace;--font-body:"Inter",sans-serif;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{-webkit-font-smoothing:antialiased;scroll-behavior:smooth}
body{font-family:var(--font-body);font-size:var(--text-base);color:var(--color-text);background:var(--color-bg);min-height:100vh;line-height:1.6}
button{cursor:pointer;background:none;border:none;font:inherit;color:inherit}

/* HEADER */
.header{position:sticky;top:0;z-index:100;background:var(--color-bg);border-bottom:1px solid var(--color-border);padding:12px 24px;display:flex;align-items:center;gap:16px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none}
.logo-icon{width:32px;height:32px;flex-shrink:0}
.logo-text{font-family:var(--font-mono);font-size:var(--text-sm);font-weight:600;color:var(--color-primary);letter-spacing:0.05em;white-space:nowrap}
.header-sub{font-size:var(--text-xs);color:var(--color-text-muted);font-family:var(--font-mono)}
.header-right{margin-left:auto;display:flex;align-items:center;gap:12px}
.stat-pill{background:var(--color-surface-offset);border:1px solid var(--color-border);border-radius:var(--radius-xl);padding:4px 12px;font-size:var(--text-xs);font-family:var(--font-mono);color:var(--color-text-muted)}
.stat-pill span{color:var(--color-primary);font-weight:600}

/* SEARCH BAR */
.search-bar{padding:16px 24px;display:flex;gap:12px;align-items:center;border-bottom:1px solid var(--color-divider)}
.search-input{flex:1;background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius-md);padding:8px 14px;font-size:var(--text-sm);color:var(--color-text);font-family:var(--font-mono);outline:none;transition:border-color 0.15s}
.search-input::placeholder{color:var(--color-text-faint)}
.search-input:focus{border-color:var(--color-primary)}
.filter-btn{background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius-md);padding:8px 14px;font-size:var(--text-xs);font-family:var(--font-mono);color:var(--color-text-muted);transition:all 0.15s;white-space:nowrap}
.filter-btn:hover,.filter-btn.active{background:var(--color-primary-glow);border-color:var(--color-primary);color:var(--color-primary)}
.filter-btn.active{font-weight:600}

/* CATEGORY TABS */
.category-tabs{padding:0 24px;display:flex;gap:4px;border-bottom:1px solid var(--color-divider);overflow-x:auto}
.cat-tab{padding:10px 16px;font-size:var(--text-xs);font-family:var(--font-mono);font-weight:500;color:var(--color-text-muted);border-bottom:2px solid transparent;white-space:nowrap;transition:all 0.15s;text-transform:uppercase;letter-spacing:0.06em}
.cat-tab:hover{color:var(--color-text)}
.cat-tab.active{color:var(--color-primary);border-bottom-color:var(--color-primary)}

/* MAIN GRID */
.main{padding:24px;display:flex;flex-direction:column;gap:8px}
.section-header{display:flex;align-items:center;gap:10px;padding:8px 0 4px;margin-top:8px}
.section-label{font-family:var(--font-mono);font-size:var(--text-xs);font-weight:600;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-text-faint)}
.section-line{flex:1;height:1px;background:var(--color-divider)}

/* TARGET CARDS */
.target-card{background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius-lg);overflow:hidden;transition:border-color 0.15s}
.target-card:hover{border-color:var(--color-border)}
.target-card.expanded{border-color:var(--color-primary)}
.card-header{display:grid;grid-template-columns:48px 1fr auto;align-items:center;gap:0;cursor:pointer;padding:14px 16px}
.card-header:hover .card-title{color:var(--color-primary)}
.card-num{font-family:var(--font-mono);font-size:var(--text-xs);color:var(--color-text-faint);font-weight:600;padding-right:12px}
.card-meta{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.card-title{font-size:var(--text-sm);font-weight:600;color:var(--color-text);transition:color 0.15s}
.card-tags{display:flex;gap:6px;flex-wrap:wrap}
.tag{font-family:var(--font-mono);font-size:10px;font-weight:600;padding:2px 8px;border-radius:var(--radius-sm);text-transform:uppercase;letter-spacing:0.06em;white-space:nowrap}
.tag-class{background:rgba(79,152,163,0.12);color:var(--color-primary);border:1px solid rgba(79,152,163,0.25)}
.tag-identity{background:rgba(168,111,223,0.12);color:var(--color-purple);border:1px solid rgba(168,111,223,0.25)}
.tag-knowledge{background:rgba(85,145,199,0.12);color:var(--color-blue);border:1px solid rgba(85,145,199,0.25)}
.tag-systems{background:rgba(232,175,52,0.12);color:var(--color-gold);border:1px solid rgba(232,175,52,0.25)}
.tag-intelligence{background:rgba(109,170,69,0.12);color:var(--color-success);border:1px solid rgba(109,170,69,0.25)}
.tag-operational{background:rgba(253,171,67,0.12);color:var(--color-orange);border:1px solid rgba(253,171,67,0.25)}
.card-toggle{font-family:var(--font-mono);font-size:var(--text-xs);color:var(--color-text-faint);padding-left:16px;transition:transform 0.15s}
.target-card.expanded .card-toggle{transform:rotate(180deg)}

/* CARD BODY */
.card-body{display:none;border-top:1px solid var(--color-divider)}
.target-card.expanded .card-body{display:block}
.card-body-inner{display:grid;grid-template-columns:1fr 1fr;gap:0}
@media(max-width:768px){.card-body-inner{grid-template-columns:1fr}}
.body-col{padding:16px 20px}
.body-col+.body-col{border-left:1px solid var(--color-divider)}
.body-section{margin-bottom:14px}
.body-section:last-child{margin-bottom:0}
.body-label{font-family:var(--font-mono);font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-text-faint);margin-bottom:6px}
.body-text{font-size:var(--text-sm);color:var(--color-text-muted);line-height:1.65}
.body-text strong{color:var(--color-text);font-weight:500}

/* CODE BLOCKS */
.code-block{background:var(--color-surface-offset);border:1px solid var(--color-border);border-radius:var(--radius-md);padding:12px 14px;font-family:var(--font-mono);font-size:var(--text-xs);color:var(--color-text-muted);line-height:1.8;margin-top:6px;overflow-x:auto}
.code-block .kw{color:var(--color-primary)}
.code-block .val{color:var(--color-gold)}
.code-block .cm{color:var(--color-text-faint)}

/* PHASE PIPELINE */
.phase-pipeline{display:flex;gap:4px;flex-wrap:wrap;margin-top:6px}
.phase{font-family:var(--font-mono);font-size:10px;padding:3px 8px;border-radius:var(--radius-sm);background:var(--color-surface-offset);border:1px solid var(--color-border);color:var(--color-text-muted);white-space:nowrap}
.phase.active-phase{background:rgba(79,152,163,0.12);border-color:rgba(79,152,163,0.3);color:var(--color-primary);font-weight:600}
.phase-arrow{color:var(--color-text-faint);font-size:10px;padding-top:3px}

/* ARTIFACT BADGE */
.artifact-badge{display:inline-flex;align-items:center;gap:6px;background:var(--color-surface-dynamic);border:1px solid var(--color-border);border-radius:var(--radius-md);padding:6px 12px;font-family:var(--font-mono);font-size:var(--text-xs);color:var(--color-text-muted);margin-top:6px}
.artifact-badge .dot{width:6px;height:6px;border-radius:50%;background:var(--color-primary)}

/* OPTIMIZATION LIST */
.opt-list{list-style:none;display:flex;flex-direction:column;gap:6px;margin-top:6px}
.opt-list li{font-size:var(--text-sm);color:var(--color-text-muted);padding-left:16px;position:relative;line-height:1.6}
.opt-list li::before{content:"→";position:absolute;left:0;color:var(--color-primary);font-family:var(--font-mono);font-size:var(--text-xs)}
.opt-list li strong{color:var(--color-text);font-weight:500}

/* INTEGRATION BADGE */
.integration-badges{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px}
.int-badge{font-family:var(--font-mono);font-size:10px;padding:3px 10px;border-radius:var(--radius-xl);font-weight:600}
.int-deepickle{background:rgba(79,152,163,0.15);color:var(--color-primary);border:1px solid rgba(79,152,163,0.3)}
.int-rve{background:rgba(168,111,223,0.15);color:var(--color-purple);border:1px solid rgba(168,111,223,0.3)}
.int-shared{background:rgba(232,175,52,0.15);color:var(--color-gold);border:1px solid rgba(232,175,52,0.3)}
.int-forge{background:rgba(109,170,69,0.15);color:var(--color-success);border:1px solid rgba(109,170,69,0.3)}

/* EMPTY STATE */
.empty-state{padding:64px 24px;text-align:center;color:var(--color-text-muted);font-family:var(--font-mono);font-size:var(--text-sm)}

/* SCROLLBAR */
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:var(--color-surface)}
::-webkit-scrollbar-thumb{background:var(--color-border);border-radius:3px}
</style>
</head>
<body>

<header class="header">
  <a class="logo" href="#">
    <svg class="logo-icon" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="DEEPICKLE">
      <rect width="32" height="32" rx="8" fill="rgba(79,152,163,0.1)"/>
      <path d="M8 10h6a6 6 0 0 1 0 12H8V10z" stroke="#4f98a3" stroke-width="1.5" fill="none"/>
      <path d="M20 10h4M20 16h4M20 22h4" stroke="#4f98a3" stroke-width="1.5" stroke-linecap="round"/>
      <circle cx="11" cy="16" r="1.5" fill="#4f98a3"/>
    </svg>
    <span class="logo-text">DEEPICKLE · IN-MODE</span>
  </a>
  <span class="header-sub">CHAT LOG MINING DOCTRINE</span>
  <div class="header-right">
    <div class="stat-pill"><span id="visibleCount">25</span> TARGETS</div>
    <div class="stat-pill">10 MISSION CLASSES</div>
    <div class="stat-pill">FORGE v1.0</div>
  </div>
</header>

<div class="search-bar">
  <input class="search-input" id="searchInput" type="text" placeholder="search targets, classes, artifacts..." autocomplete="off">
  <button class="filter-btn active" data-filter="all">ALL</button>
  <button class="filter-btn" data-filter="identity">IDENTITY</button>
  <button class="filter-btn" data-filter="knowledge">KNOWLEDGE</button>
  <button class="filter-btn" data-filter="systems">SYSTEMS</button>
  <button class="filter-btn" data-filter="intelligence">INTELLIGENCE</button>
  <button class="filter-btn" data-filter="operational">OPERATIONAL</button>
</div>

<div id="categoryTabs" class="category-tabs">
  <button class="cat-tab active" data-cat="all">ALL TARGETS</button>
  <button class="cat-tab" data-cat="A">CLASS A · DETERMINISTIC</button>
  <button class="cat-tab" data-cat="G">CLASS G · LONGITUDINAL</button>
  <button class="cat-tab" data-cat="D">CLASS D · DELTA</button>
  <button class="cat-tab" data-cat="H">CLASS H · LENS</button>
  <button class="cat-tab" data-cat="I">CLASS I · EVIDENCE LEDGER</button>
</div>

<main class="main" id="targetGrid"></main>

<script>
const TARGETS = [
  // ─── IDENTITY & SELF-MODEL ───────────────────────────────────────────────
  {
    id:1, cat:"identity", missionClass:"G", title:"Mental Model Registry",
    tagCategory:"IDENTITY",
    lens:"Extract every named framework, heuristic, analogy, or conceptual structure you've applied — from Gollwitzer to Prochaska to STROT. Maps the actual operating vocabulary of your mind.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F7)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F7)","MAP"],
    extractOps:[
      "FAMILY 7 OPPORTUNITY/CONCEPT: extract all named frameworks and models",
      "FAMILY 6 QUOTABLE: pull exact formulations and definitions",
      "FAMILY 5 STRUCTURAL: headings that name frameworks across threads",
      "CONCEPT INDEX: build recurrence frequency per model"
    ],
    artifact:"concept-index + corpus-findings-memo",
    inOpt:[
      "<strong>Chunking policy:</strong> chunk by conversation turn, not paragraph — models shift between turns",
      "<strong>Extraction target:</strong> regex for capitalized compound phrases + 'the X model' patterns",
      "<strong>Concept indexing:</strong> merge near-duplicates (TTM / stages-of-change / Prochaska) into canonical entries",
      "<strong>Synthesis:</strong> produce ranked table of models by frequency × depth of application",
      "<strong>Writeback:</strong> promote top-20 to DEEPICKLE glossary; feed to RVE shared.db conceptIndex"
    ],
    integrations:["DEEPICKLE","RVE","SHARED"],
    rveLink:"Feeds RVE's if_then_plans and domain knowledge layer"
  },
  {
    id:2, cat:"identity", missionClass:"H", title:"Contradiction Map",
    tagCategory:"IDENTITY",
    lens:"Find every place where what you said you'd do, believed, or planned conflicts with what you later said, did, or abandoned. Maps the gap between declared intent and revealed behavior.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT","MAP","SYNTHESIZE"],
    keyActive:["MAP","SYNTHESIZE"],
    extractOps:[
      "FAMILY 8 CLAIM SEEDS: capture all declarative intent statements ('I will...', 'The plan is...')",
      "FAMILY 5 STRUCTURAL: extract TODO/goal markers across time-sorted corpus",
      "CLAIM SEED REGISTRY: time-stamp each claim, cross-reference with later threads",
      "CONTRADICTION MAP: build table of claim vs. counter-claim per domain"
    ],
    artifact:"contradiction-map + delta-report",
    inOpt:[
      "<strong>Sort corpus chronologically</strong> before chunking — time-ordering is essential for delta detection",
      "<strong>Claim extraction:</strong> target first-person future-tense statements and committed plans",
      "<strong>Cross-reference pass:</strong> for each claim, check if later corpus confirms, contradicts, or drops it",
      "<strong>Map output:</strong> contradiction table with columns: Claim | Date | Counter-Evidence | Resolution Status",
      "<strong>Evil Morty pass:</strong> run adversarial critic over contradiction map before synthesis"
    ],
    integrations:["DEEPICKLE","RVE"],
    rveLink:"Feeds RVE drift detection and postpone_count logic refinement"
  },
  {
    id:3, cat:"identity", missionClass:"G", title:"Behavioral Pattern Dossier",
    tagCategory:"IDENTITY",
    lens:"Mine for recurring behavioral loops — avoidance patterns, friction signatures, recurring stall points, productive flow states, and emotional triggers — across the entire chat corpus.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT","MAP"],
    extractOps:[
      "FAMILY 8 CLAIM SEEDS: extract friction/avoidance language markers",
      "FAMILY 5 STRUCTURAL: capture 'stuck', 'blocked', 'keep failing to', 'again' patterns",
      "CONCEPT INDEX: cluster into named behavioral archetypes",
      "CHRONOLOGY MAP: plot pattern recurrence over time"
    ],
    artifact:"behavioral-intervention-memo + lens-run",
    inOpt:[
      "<strong>Lexical extraction:</strong> build targeted regex for avoidance vocabulary ('keep meaning to', 'still haven't', 'again I...', 'blocked by')",
      "<strong>Cluster by domain:</strong> separate patterns by RVE domain_id (recovery, coding, school)",
      "<strong>Frequency × recency scoring:</strong> weight recent recurrences higher for intervention priority",
      "<strong>Cross-reference TTM stage:</strong> map each pattern to Prochaska stage for RVE stage-matched interventions",
      "<strong>Writeback:</strong> high-frequency patterns feed RVE habit.trigger field and if_then_plans table"
    ],
    integrations:["DEEPICKLE","RVE","FORGE"],
    rveLink:"Direct feed to RVE habit_log and if_then_plans"
  },
  {
    id:4, cat:"identity", missionClass:"I", title:"Self-Calibration Ledger",
    tagCategory:"IDENTITY",
    lens:"Extract every instance where you estimated something (time, difficulty, confidence, readiness) and compare with later actual reports. Builds evidence of your systematic self-model biases.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT","MAP"],
    extractOps:[
      "FAMILY 3 TEMPORAL: extract time estimates ('this should take...', 'about X hours')",
      "FAMILY 8 CLAIM SEEDS: capture confidence and difficulty estimates",
      "EVIDENCE LEDGER: pair estimates with outcome reports from later threads",
      "CALIBRATION MAP: estimate vs. actual deviation table"
    ],
    artifact:"evidence-ledger + calibration-memo",
    inOpt:[
      "<strong>Two-pass extraction:</strong> Pass 1 extracts estimates, Pass 2 extracts completions/outcomes — pair by task/project identity",
      "<strong>Deviation scoring:</strong> calculate % over/under for time and difficulty systematically",
      "<strong>Bias classification:</strong> classify each deviation as optimism-bias, friction-underestimate, or scope-creep",
      "<strong>Writeback:</strong> calibration findings feed RVE score.py adjustment coefficients",
      "<strong>Artifact:</strong> evidence ledger with fields: TaskID | Estimate | Actual | Deviation% | BiasType"
    ],
    integrations:["DEEPICKLE","RVE","FORGE"],
    rveLink:"Feeds RVE score.py calibration adjustments"
  },
  {
    id:5, cat:"identity", missionClass:"H", title:"Recovery Context Map",
    tagCategory:"IDENTITY",
    lens:"Mine for recovery-relevant signals — triggers, relapse-risk patterns, support structures referenced, motivational framings that worked, and emotional tone correlating with productive vs. difficult periods.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT","MAP","SYNTHESIZE"],
    keyActive:["MAP","SYNTHESIZE"],
    extractOps:[
      "FAMILY 8 CLAIM SEEDS: capture recovery-related assertions and commitments",
      "FAMILY 5 STRUCTURAL: extract treatment/program references and milestone dates",
      "LENS: Recovery Resilience — filter corpus through what strengthens vs. threatens sobriety",
      "CHRONOLOGY MAP: plot recovery context against productivity and emotional tone"
    ],
    artifact:"behavioral-intervention-memo",
    inOpt:[
      "<strong>Recovery lens is primary:</strong> this is CLASS H — one lens, applied rigorously, no scope drift",
      "<strong>PII sensitivity:</strong> this corpus stays strictly local — no external routing of recovery content",
      "<strong>Trigger vocabulary extraction:</strong> targeted lexical pass for known high-risk language patterns",
      "<strong>Temporal correlation:</strong> overlay recovery timeline with output quality and stated energy",
      "<strong>Writeback:</strong> resilience patterns feed RVE profile and if_then_plan cue→response library"
    ],
    integrations:["RVE","FORGE"],
    rveLink:"Feeds RVE profile recovery_context and if_then_plans"
  },
  // ─── KNOWLEDGE & CAPABILITY ACQUISITION ──────────────────────────────────
  {
    id:6, cat:"knowledge", missionClass:"A", title:"Conceptual Vocabulary Index",
    tagCategory:"KNOWLEDGE",
    lens:"Extract every coined term, redefined concept, novel phrase, and specialized vocabulary that has emerged across your AI interactions — building the operational glossary of your intellectual framework.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F5,F6)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F5,F6)","MAP"],
    extractOps:[
      "FAMILY 5 STRUCTURAL: extract all section headings and bold/capitalized terms",
      "FAMILY 6 QUOTABLE: pull exact definitions and canonical formulations",
      "CONCEPT INDEX: build per-term frequency, first-seen, last-seen, source anchors",
      "FAMILY 8 CLAIM SEEDS: definitions stated as doctrines ('X means...', 'X is...')"
    ],
    artifact:"concept-index + glossary",
    inOpt:[
      "<strong>TF-IDF approach:</strong> terms appearing in YOUR corpus but rare in generic text are high-signal",
      "<strong>Alias merging:</strong> script pass to cluster near-identical terms before model-assisted canonicalization",
      "<strong>Frequency × recency weighting:</strong> terms used recently AND frequently are highest-priority",
      "<strong>Promotion threshold:</strong> terms with frequency ≥ 3 across ≥ 2 sessions → promote to DEEPICKLE glossary",
      "<strong>Writeback:</strong> full concept index feeds shared.db glossary table for RVE+DEEPICKLE shared vocabulary"
    ],
    integrations:["DEEPICKLE","RVE","SHARED"],
    rveLink:"Shared glossary in shared.db — both systems reason from same vocabulary"
  },
  {
    id:7, cat:"knowledge", missionClass:"H", title:"Domain Cross-Pollination Map",
    tagCategory:"KNOWLEDGE",
    lens:"Find every instance where a concept from one domain was applied to another — behavioral science to AI architecture, martial arts to security, music production to prompt engineering. Your greatest intellectual asset.",
    phases:["INTAKE","NORMALIZE","CHUNK","MAP","SYNTHESIZE"],
    keyActive:["MAP","SYNTHESIZE"],
    extractOps:[
      "CONCEPT INDEX: tag each concept with domain of origin",
      "RELATIONS TABLE: capture 'applied-to' edges between (concept, source-domain, target-domain)",
      "FAMILY 6 QUOTABLE: pull exact cross-domain analogies and framings",
      "LENS: Cross-Pollination — scan for 'like X but for Y' constructions and domain metaphors"
    ],
    artifact:"opportunity-map + lens-run",
    inOpt:[
      "<strong>Domain taxonomy first:</strong> define your domain list (matches RVE domains) before extraction",
      "<strong>Relation extraction:</strong> use rg to find 'is like', 'same as', 'apply X to Y', 'inspired by' patterns",
      "<strong>Graph construction:</strong> build directed graph of domain→concept→domain transfer edges",
      "<strong>Gap analysis:</strong> identify domain pairs with no cross-pollination yet — highest opportunity nodes",
      "<strong>Writeback:</strong> top 10 cross-pollination opportunities become IDEAS in RVE idea pipeline"
    ],
    integrations:["DEEPICKLE","RVE"],
    rveLink:"Top opportunities → RVE ideas table with stage=contemplation"
  },
  {
    id:8, cat:"knowledge", missionClass:"G", title:"Skill Acquisition Timeline",
    tagCategory:"KNOWLEDGE",
    lens:"Reconstruct a chronological map of every skill you've explored, studied, or partially acquired — showing depth indicators (surface/working/deep) and recency to identify what's compounding vs. stalling.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F3,F5)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F3,F5)","MAP"],
    extractOps:[
      "FAMILY 3 TEMPORAL: extract dates of first engagement with each skill domain",
      "FAMILY 5 STRUCTURAL: extract skill/topic headings and learning-context markers",
      "CHRONOLOGY MAP: plot skill engagement over time",
      "CONCEPT INDEX: tag skills with depth indicators from context depth"
    ],
    artifact:"corpus-findings-memo + opportunity-map",
    inOpt:[
      "<strong>Chronological corpus sort</strong> is mandatory before extraction — timeline is the primary output",
      "<strong>Depth scoring heuristic:</strong> count conversation-turns-per-skill as a proxy for depth investment",
      "<strong>Recency weighting:</strong> skills touched in last 30 days are 'active'; 90+ days 'stalled'; 6mo+ 'dormant'",
      "<strong>Compound vs. shallow classification:</strong> skills where each session built on the prior = compound",
      "<strong>Writeback:</strong> active compound skills → RVE projects; dormant high-value skills → RVE ideas pipeline"
    ],
    integrations:["DEEPICKLE","RVE"],
    rveLink:"Active skills → RVE projects table; dormant → ideas table"
  },
  {
    id:9, cat:"knowledge", missionClass:"D", title:"Knowledge Gap Registry",
    tagCategory:"KNOWLEDGE",
    lens:"Questions asked repeatedly across your corpus are the deepest unsolved problems in your intellectual life. Extract them, cluster them, and build a priority registry of genuine knowledge gaps.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT","MAP"],
    extractOps:[
      "FAMILY 8 CLAIM SEEDS: extract questions posed (interrogative sentence forms)",
      "CONCEPT INDEX: cluster questions by topic and domain",
      "FREQUENCY ANALYSIS: questions asked 3+ times = genuine persistent gap",
      "DELTA: compare gap questions against answers/resolutions found in later threads"
    ],
    artifact:"delta-report + opportunity-map",
    inOpt:[
      "<strong>Interrogative extraction:</strong> rg pattern for '?' lines across all chunks",
      "<strong>Semantic deduplication:</strong> model-assisted clustering of paraphrased versions of the same question",
      "<strong>Resolution check:</strong> for each gap question, run delta pass to see if any later thread answered it",
      "<strong>Unresolved high-frequency gaps → OUT mission seeds</strong> for DEEPICKLE research runs",
      "<strong>Writeback:</strong> top-10 unresolved gaps become DEEPICKLE OUT mission candidates and RVE project seeds"
    ],
    integrations:["DEEPICKLE","RVE"],
    rveLink:"Unresolved gaps → DEEPICKLE OUT mission queue"
  },
  {
    id:10, cat:"knowledge", missionClass:"G", title:"Compound Interest Tracker",
    tagCategory:"KNOWLEDGE",
    lens:"Find every topic where your understanding has deepened conversation-by-conversation — where you're not repeating questions but building on prior answers. These are your highest-leverage intellectual investment zones.",
    phases:["INTAKE","NORMALIZE","CHUNK","MAP","SYNTHESIZE"],
    keyActive:["MAP","SYNTHESIZE"],
    extractOps:[
      "LONGITUDINAL THREAD MINING: track concept depth progression over time per topic",
      "CONCEPT INDEX: first-seen vs last-seen depth comparison",
      "CHRONOLOGY MAP: plot depth trajectory — increasing, plateau, or declining engagement",
      "DELTA: compare early vs late treatment of same topic for evidence of depth gain"
    ],
    artifact:"opportunity-map + corpus-findings-memo",
    inOpt:[
      "<strong>Depth proxy scoring:</strong> question complexity, vocabulary specificity, and prerequisite density increase = depth gain",
      "<strong>Trajectory classification:</strong> Rising (active compound), Plateau (maintenance), Declining (fading), Spiked (one-off)",
      "<strong>ROI scoring:</strong> depth-gain rate × practical application frequency = compound interest score",
      "<strong>Rising topics = scheduling priority</strong> for RVE's high_cognitive energy blocks",
      "<strong>Writeback:</strong> top compound topics → RVE projects with compound_val = 10"
    ],
    integrations:["DEEPICKLE","RVE"],
    rveLink:"Feeds RVE compound_val scoring for task prioritization"
  },
  // ─── SYSTEMS & PROJECTS ───────────────────────────────────────────────────
  {
    id:11, cat:"systems", missionClass:"B", title:"Project Archaeology Map",
    tagCategory:"SYSTEMS",
    lens:"Reconstruct every project mentioned across your entire AI chat history — its genesis, current or last-known stage, completion fate (done/stalled/abandoned/evolved), and the reasons for its trajectory.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F4)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F4)","MAP"],
    extractOps:[
      "FAMILY 4 ENTITY: extract project/system names and their variations",
      "FAMILY 3 TEMPORAL: anchor each project to its first mention and last mention dates",
      "CHRONOLOGY MAP: plot project lifecycle states over time",
      "FAMILY 8 CLAIM SEEDS: capture stated reasons for stalling or pivoting"
    ],
    artifact:"corpus-findings-memo + delta-report",
    inOpt:[
      "<strong>Entity resolution:</strong> DEEPICKLE/Pickle Rick/DeePickle are one entity — deduplicate with alias mapping",
      "<strong>Stage classification:</strong> map last-known state to RVE's lifecycle states (captured/in_progress/stalled/archived)",
      "<strong>Fate scoring:</strong> completed projects score 1, stalled projects score by cascade_val of what they'd unlock",
      "<strong>Archaeology output:</strong> master project table with genesis date, stage, fate, reason, and recovery potential",
      "<strong>Writeback:</strong> stalled high-value projects → RVE tasks table with state=blocked + context in notes"
    ],
    integrations:["DEEPICKLE","RVE","SHARED"],
    rveLink:"Stalled projects → RVE tasks with context-rich action plans"
  },
  {
    id:12, cat:"systems", missionClass:"D", title:"Design Evolution Delta Log",
    tagCategory:"SYSTEMS",
    lens:"Track how DEEPICKLE, RVE, Pickle Rick, and related system designs changed across conversations — finding what was proposed but not built, what was abandoned and why, and where the current design diverges from prior intent.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT","MAP"],
    extractOps:[
      "FAMILY 8 CLAIM SEEDS: capture architectural decisions and design declarations",
      "DELTA EXTRACTION: compare design statements across time — what changed?",
      "FAMILY 3 TEMPORAL: anchor each design iteration to its conversation date",
      "CONTRADICTION MAP: find declared features that were later dropped or changed"
    ],
    artifact:"delta-report + blueprint",
    inOpt:[
      "<strong>Version-ordered corpus sort</strong> is mandatory — must process old→new to detect evolution direction",
      "<strong>Diff framing:</strong> for each component (FORGE, ENGINE, ARSENAL), find earliest vs. latest specification",
      "<strong>Unrealized-feature delta:</strong> items declared in design docs but absent from build order = highest-value deltas",
      "<strong>Abandoned rationale mining:</strong> look for 'not yet', 'later', 'defer' near high-value design claims",
      "<strong>Writeback:</strong> top-5 unrealized deltas → DEEPICKLE artifact index as blueprint seeds"
    ],
    integrations:["DEEPICKLE","FORGE"],
    rveLink:"Design evolution feeds DEEPICKLE's own AUDIT phase"
  },
  {
    id:13, cat:"systems", missionClass:"D", title:"Stalled Thread Registry",
    tagCategory:"SYSTEMS",
    lens:"Identify every conversation thread that began something significant — a build, a plan, a framework, a research task — but was never completed, never implemented, or was abandoned mid-stream. These are the buried assets.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT","SYNTHESIZE"],
    extractOps:[
      "FAMILY 5 STRUCTURAL: extract conversation starts with clear 'begin building X' intent",
      "DELTA: check if later corpus shows completion or continuation of these starts",
      "FAMILY 3 TEMPORAL: age of stall — how long since last touch?",
      "FAMILY 7 OPPORTUNITY: classify recovery potential (high/medium/low) per stalled thread"
    ],
    artifact:"opportunity-map + delta-report",
    inOpt:[
      "<strong>Stall detection heuristic:</strong> conversation has clear initiation + 0 later follow-up threads = stalled",
      "<strong>Recovery potential scoring:</strong> stalled + high cascade_val + low re-entry friction = highest priority recoveries",
      "<strong>Classify stall type:</strong> Context-Lost (recoverable), Superseded (intentionally replaced), Blocked (external), Abandoned (friction)",
      "<strong>Re-entry cost estimation:</strong> small re-entry cost + high output value = immediate recovery candidate",
      "<strong>Writeback:</strong> top recoveries → RVE tasks in onboarding_pending state with stall context in notes"
    ],
    integrations:["DEEPICKLE","RVE"],
    rveLink:"Recovered threads → RVE task reservoir with stall context"
  },
  {
    id:14, cat:"systems", missionClass:"A", title:"Instruction Engineering Library",
    tagCategory:"SYSTEMS",
    lens:"Extract every system prompt, custom instruction, GEMINI.md content, prompt chain, and prompt-priming framework you've designed or co-designed across your AI interactions.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F5,F6)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F5,F6)","MAP"],
    extractOps:[
      "FAMILY 5 STRUCTURAL: extract all GEMINI.md contents, system prompts, and instruction blocks",
      "FAMILY 6 QUOTABLE: pull exact prompt formulations that worked well",
      "ENTITY: catalog by target system (Gemini CLI, Claude, Perplexity, ChatGPT)",
      "CONCEPT INDEX: cluster by purpose (persona, task-routing, validator, behavioral)"
    ],
    artifact:"corpus-findings-memo + ledger",
    inOpt:[
      "<strong>Normalization by target system:</strong> separate Gemini-specific from general patterns early",
      "<strong>Pattern classification:</strong> Persona prompts / Task-routing / Validator instructions / Behavioral constraints",
      "<strong>Effectiveness tagging:</strong> mine adjacent conversation for operator feedback on each prompt version",
      "<strong>Version delta:</strong> track how each prompt evolved to find what specifically improved performance",
      "<strong>Writeback:</strong> best-of-class prompts become canonical entries in DEEPICKLE's instruction library module"
    ],
    integrations:["DEEPICKLE","RVE","SHARED"],
    rveLink:"Best prompts → GEMINI.md update candidates for both RVE and DEEPICKLE"
  },
  {
    id:15, cat:"systems", missionClass:"A", title:"Implementation Intention Archive",
    tagCategory:"SYSTEMS",
    lens:"Extract every if-then plan, cue→response script, friction-response commitment, and implementation intention across all chat history. Builds a canonical library of the if-then logic you've designed for yourself.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F8)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F8)","MAP"],
    extractOps:[
      "FAMILY 8 CLAIM SEEDS: 'If X then Y', 'When X → do Y', 'After X → switch to Y'",
      "FAMILY 5 STRUCTURAL: extract any formatted cue-response plans",
      "ENTITY: link each if-then to its domain and trigger context",
      "DELTA: check which plans appear in multiple sessions = durable doctrine"
    ],
    artifact:"ledger + corpus-findings-memo",
    inOpt:[
      "<strong>Regex patterns:</strong> 'if.*then', 'when.*→', 'after.*I will', 'instead of.*I', 'trigger.*response'",
      "<strong>Deduplication:</strong> merge identical or near-identical plans from different sessions",
      "<strong>Validation check:</strong> for each plan, mine corpus for evidence of actual deployment vs. theoretical-only",
      "<strong>Activation scoring:</strong> plans mentioned 3+ times = canonical; single-mention = provisional",
      "<strong>Writeback:</strong> canonical plans populate RVE if_then_plans table directly"
    ],
    integrations:["DEEPICKLE","RVE","FORGE"],
    rveLink:"Direct import to RVE if_then_plans table"
  },
  // ─── INTELLIGENCE PRODUCTION ──────────────────────────────────────────────
  {
    id:16, cat:"intelligence", missionClass:"D", title:"Idea Pipeline Seed Bank",
    tagCategory:"INTELLIGENCE",
    lens:"Every idea mentioned but not developed, every 'what if' that was dropped, every promising tangent that didn't become a project. This is your buried idea inventory.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F7,F8)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F7,F8)","MAP"],
    extractOps:[
      "FAMILY 7 OPPORTUNITY: capture ideas flagged but not acted upon",
      "FAMILY 8 CLAIM SEEDS: 'could be interesting to', 'worth exploring', 'someday I want to'",
      "DELTA: compare idea mentions to later corpus — developed or abandoned?",
      "FAMILY 3 TEMPORAL: age and recurrence of each idea"
    ],
    artifact:"opportunity-map",
    inOpt:[
      "<strong>Idea signals:</strong> 'could', 'might', 'what if', 'imagine if', 'someday', 'worth exploring'",
      "<strong>TTM stage assignment:</strong> classify each idea by Prochaska stage based on language depth and recurrence",
      "<strong>Novelty scoring:</strong> ideas with no resolution AND high recurrence = highest unconscious priority",
      "<strong>Feasibility pre-screen:</strong> filter for ideas achievable at current constraint level (no money, local-first)",
      "<strong>Writeback:</strong> top ideas → RVE ideas table with stage, domain, and why fields populated"
    ],
    integrations:["DEEPICKLE","RVE"],
    rveLink:"Feeds RVE ideas table directly with stage and domain classification"
  },
  {
    id:17, cat:"intelligence", missionClass:"A", title:"Reference Corpus Seed List",
    tagCategory:"INTELLIGENCE",
    lens:"Extract every source, paper, book, URL, author, tool, and resource that was mentioned as valuable, interesting, or worth reading across all chat history. Build your canonical reference reservoir from your own discovery trail.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F1,F2,F4)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F1,F2,F4)","MAP"],
    extractOps:[
      "FAMILY 2 WEB SOURCE: extract all URLs, domains, and repository references",
      "FAMILY 4 ENTITY: extract author names, paper titles, book titles",
      "FAMILY 6 QUOTABLE: capture accompanying quality assessments ('excellent', 'canonical', 'gold-standard')",
      "SOURCE RESERVOIR: classify each by domain and mission-class fit"
    ],
    artifact:"ledger + source-reservoir",
    inOpt:[
      "<strong>URL normalization:</strong> deduplicate URLs, resolve redirects in post-processing",
      "<strong>Quality signal extraction:</strong> mine adjacent text for operator endorsement strength",
      "<strong>Accessibility check:</strong> tag as public/paywalled/download-required",
      "<strong>Domain classification:</strong> assign each source to DEEPICKLE mission classes it serves",
      "<strong>Writeback:</strong> top-tier sources populate DEEPICKLE source_reservoir in shared.db"
    ],
    integrations:["DEEPICKLE","SHARED"],
    rveLink:"Feeds DEEPICKLE source_reservoir and supersource registry"
  },
  {
    id:18, cat:"intelligence", missionClass:"C", title:"Writing Sample Corpus",
    tagCategory:"INTELLIGENCE",
    lens:"Collect and classify every substantial piece of writing you've produced in AI sessions — by artifact class, rhetorical mode, quality tier, and purpose. Builds your personal gold-standard specimen set.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT","SYNTHESIZE"],
    extractOps:[
      "FAMILY 6 QUOTABLE: extract all multi-paragraph prose blocks you authored",
      "FAMILY 5 STRUCTURAL: classify by heading structure and section architecture",
      "ARTIFACT CLASS: map each piece to DEEPICKLE output classes (memo, essay, blueprint, etc.)",
      "QUALITY SCORING: apply writing validator rubric to each extracted piece"
    ],
    artifact:"corpus-findings-memo + ledger",
    inOpt:[
      "<strong>Authorship detection:</strong> distinguish your prose from AI prose — mine your own voice specifically",
      "<strong>Class assignment:</strong> run artifact completeness validator against each piece to assign output class",
      "<strong>Quality tier:</strong> apply writing validator (truth preservation, structure, specificity, anti-bloat)",
      "<strong>Voice fingerprint:</strong> extract recurring rhetorical patterns, sentence structures, and vocabulary that are distinctly yours",
      "<strong>Writeback:</strong> top pieces become DEEPICKLE's internal gold-standard specimens for validator calibration"
    ],
    integrations:["DEEPICKLE","FORGE"],
    rveLink:"Best writing samples inform DEEPICKLE's writing validator thresholds"
  },
  {
    id:19, cat:"intelligence", missionClass:"I", title:"Hypothesis Registry",
    tagCategory:"INTELLIGENCE",
    lens:"Extract every explicit and implicit hypothesis about how systems work, how people behave, how you function, or how the world operates. Build an evidence-linked registry of your working theories.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F8)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F8)","MAP"],
    extractOps:[
      "FAMILY 8 CLAIM SEEDS: 'I think X causes Y', 'my hypothesis is', 'probably because', 'the reason X happens is'",
      "CLAIM REGISTRY: catalog each hypothesis with claim type and confidence level",
      "EVIDENCE LEDGER: link each hypothesis to supporting or contradicting evidence",
      "CONTRADICTION MAP: find hypotheses that contradict each other"
    ],
    artifact:"claim-registry + evidence-ledger",
    inOpt:[
      "<strong>Hypothesis signal vocabulary:</strong> 'because', 'causes', 'leads to', 'I think', 'probably', 'likely', 'suspect'",
      "<strong>Confidence calibration:</strong> classify by hedging language strength (certain/probable/speculative)",
      "<strong>Evidence linking:</strong> for each hypothesis, mine later corpus for confirming/disconfirming observations",
      "<strong>ACH matrix:</strong> for competing hypotheses about the same question, run Analysis of Competing Hypotheses",
      "<strong>Writeback:</strong> high-confidence hypotheses promote to DEEPICKLE doctrine; low-confidence → OUT research queue"
    ],
    integrations:["DEEPICKLE","SHARED"],
    rveLink:"Behavioral hypotheses feed RVE's if_then design and domain modeling"
  },
  {
    id:20, cat:"intelligence", missionClass:"D", title:"Opportunity Database",
    tagCategory:"INTELLIGENCE",
    lens:"Mine for every grant, program, tool, career path, income stream, collaboration, or resource that was mentioned as relevant but never pursued. Maps the unrealized opportunity landscape of your AI conversations.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F7)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F7)","MAP"],
    extractOps:[
      "FAMILY 7 OPPORTUNITY: grants, programs, resources, jobs, tools, income paths",
      "FAMILY 2 WEB SOURCE: URLs for actionable opportunities",
      "FAMILY 3 TEMPORAL: deadline or time-sensitivity information",
      "DELTA: opportunities mentioned in past but never acted on = highest-value delta targets"
    ],
    artifact:"opportunity-map",
    inOpt:[
      "<strong>Constraint filter first:</strong> all opportunities must pass current-constraint screen (no money, local-first, housing-limited)",
      "<strong>Time-sensitivity scoring:</strong> deadline-bound opportunities auto-elevated to urgent",
      "<strong>Cascade value scoring:</strong> opportunities that unlock multiple downstream paths score highest",
      "<strong>Action cost estimation:</strong> classify by activation cost — low-friction opportunities prioritized for immediate capture",
      "<strong>Writeback:</strong> top opportunities → RVE tasks with urgency, impact, cascade_val fields populated"
    ],
    integrations:["DEEPICKLE","RVE","SHARED"],
    rveLink:"Direct feed to RVE task reservoir with pre-scored metric fields"
  },
  // ─── OPERATIONAL INTELLIGENCE ─────────────────────────────────────────────
  {
    id:21, cat:"operational", missionClass:"G", title:"Question Archaeology",
    tagCategory:"OPERATIONAL",
    lens:"The questions you keep returning to are your deepest unsolved problems. Extract, cluster, and count every question asked across all sessions to build a frequency-ranked map of your genuine persistent unknowns.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT","MAP"],
    extractOps:[
      "DETERMINISTIC: extract all '?' terminated sentences across entire corpus",
      "CONCEPT INDEX: cluster questions by topic domain and question type",
      "FREQUENCY COUNT: questions asked 3+ times = persistent gap",
      "CHRONOLOGY MAP: when was each question first asked? How often returned to?"
    ],
    artifact:"corpus-findings-memo + opportunity-map",
    inOpt:[
      "<strong>Pure deterministic extraction first:</strong> rg '\?' across all chunks — no model needed",
      "<strong>Deduplication pass:</strong> semantic clustering to collapse paraphrased versions",
      "<strong>Frequency histogram:</strong> visual distribution of question recurrence counts",
      "<strong>Top-10 persistent questions → DEEPICKLE OUT missions</strong> — these are your most valuable research targets",
      "<strong>Writeback:</strong> unresolved top questions → shared.db as open research missions with OUT mission class"
    ],
    integrations:["DEEPICKLE","RVE","SHARED"],
    rveLink:"Persistent questions become DEEPICKLE OUT mission seeds"
  },
  {
    id:22, cat:"operational", missionClass:"I", title:"Decision Audit Trail",
    tagCategory:"OPERATIONAL",
    lens:"Reconstruct every significant decision made with AI assistance — what the options were, what was chosen, why, and what the outcome was. Build an evidence ledger of your decision-making quality and patterns.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F8)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F8)","MAP"],
    extractOps:[
      "FAMILY 8 CLAIM SEEDS: 'I decided', 'going with', 'choosing X over Y', 'the decision is'",
      "EVIDENCE LEDGER: link each decision to its options, rationale, and later outcome",
      "FAMILY 3 TEMPORAL: decision date and outcome assessment date",
      "CONTRADICTION MAP: decisions reversed or regretted in later corpus"
    ],
    artifact:"evidence-ledger + lens-run",
    inOpt:[
      "<strong>Decision signal vocabulary:</strong> 'going to', 'decided', 'chose', 'picked', 'will use', 'instead of X, Y'",
      "<strong>Option set reconstruction:</strong> mine pre-decision context for what alternatives were considered",
      "<strong>Outcome tracing:</strong> find later corpus references to each decision's consequences",
      "<strong>Decision quality scoring:</strong> alignment with stated values × outcome quality = decision score",
      "<strong>Writeback:</strong> decision patterns feed RVE's if_then_plans and inform DEEPICKLE's operator memo artifact class"
    ],
    integrations:["DEEPICKLE","RVE"],
    rveLink:"Decision patterns inform RVE checkpoint templates"
  },
  {
    id:23, cat:"operational", missionClass:"A", title:"Tool & Resource Discovery Log",
    tagCategory:"OPERATIONAL",
    lens:"Extract every tool, software package, CLI utility, API, library, platform, service, or technique that was discovered or discussed across your AI interactions. Builds your complete discovered-technology inventory.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F1,F2,F4)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F1,F2,F4)","MAP"],
    extractOps:[
      "FAMILY 2 WEB SOURCE: URLs pointing to tools and repositories",
      "FAMILY 4 ENTITY: tool/library/service names with context",
      "FAMILY 1 CONTACT: relevant installation/access patterns",
      "CONCEPT INDEX: classify by category (CLI, Python, AI, security, mobile, etc.)"
    ],
    artifact:"ledger + opportunity-map",
    inOpt:[
      "<strong>Tech name extraction:</strong> regex patterns for common naming conventions (camelCase, kebab-case packages, v-prefixed versions)",
      "<strong>Installation status tagging:</strong> mine corpus for evidence of actual use vs. theoretical discovery",
      "<strong>Constraint filtering:</strong> local-first, free/open-source, Windows/WSL-compatible = current filter",
      "<strong>Recency scoring:</strong> tools mentioned in recent sessions weighted higher",
      "<strong>Writeback:</strong> unused high-value tools → RVE tasks (domain: coding_tech, energy_type: high_cognitive)"
    ],
    integrations:["DEEPICKLE","RVE","SHARED"],
    rveLink:"Unused high-value tools → RVE tasks with cascade_val scoring"
  },
  {
    id:24, cat:"operational", missionClass:"H", title:"Prompt Engineering Pattern Library",
    tagCategory:"OPERATIONAL",
    lens:"Mine for every effective prompt pattern, framing technique, and prompt structure that demonstrably improved AI output quality across your sessions. Build your canonical personal prompt library.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F5,F6)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F5,F6)","MAP"],
    extractOps:[
      "FAMILY 5 STRUCTURAL: extract prompt blocks, system instruction sections, framing patterns",
      "FAMILY 6 QUOTABLE: pull exact formulations of effective framings",
      "LENS: Prompt Effectiveness — what framings preceded notably better AI responses?",
      "CONCEPT INDEX: cluster patterns by technique type (chain-of-thought, persona, validator, etc.)"
    ],
    artifact:"ledger + corpus-findings-memo",
    inOpt:[
      "<strong>Effectiveness proxy:</strong> prompts followed by long, detailed, praised AI responses = higher effectiveness signal",
      "<strong>Pattern taxonomy:</strong> Persona-setting / Task-specification / Constraint-injection / Output-class-declaration / Validator-injection",
      "<strong>Cross-platform tagging:</strong> what works for Gemini vs. Claude vs. Perplexity may differ",
      "<strong>Anti-pattern mining:</strong> also extract framings that preceded poor or refused outputs",
      "<strong>Writeback:</strong> top patterns → GEMINI.md update candidates and DEEPICKLE's instruction engineering module"
    ],
    integrations:["DEEPICKLE","RVE","SHARED"],
    rveLink:"Best patterns update GEMINI.md for both RVE and DEEPICKLE contexts"
  },
  {
    id:25, cat:"operational", missionClass:"G", title:"Temporal Life State Timeline",
    tagCategory:"OPERATIONAL",
    lens:"Reconstruct a chronological narrative of your life from the AI conversation record — housing transitions, sobriety milestones, project launches, school events, relationship changes, emotional landmarks. The longitudinal life snapshot.",
    phases:["INTAKE","NORMALIZE","CHUNK","EXTRACT(F3,F4)","MAP","SYNTHESIZE"],
    keyActive:["EXTRACT(F3,F4)","MAP"],
    extractOps:[
      "FAMILY 3 TEMPORAL: all date references, milestone markers, 'today', 'yesterday', 'last week'",
      "FAMILY 4 ENTITY: people, places, institutions mentioned with temporal context",
      "CHRONOLOGY MAP: absolute timeline anchored to conversation dates",
      "FAMILY 8 CLAIM SEEDS: status-change declarations ('I moved', 'I started', 'I got', 'I lost')"
    ],
    artifact:"corpus-findings-memo + evidentiary-report",
    inOpt:[
      "<strong>Conversation metadata is primary anchor:</strong> use file timestamps as ground truth for chronological ordering",
      "<strong>Relative→absolute resolution:</strong> 'yesterday' resolved to actual date from conversation timestamp",
      "<strong>Life domain tagging:</strong> tag each event with RVE domain (recovery, school, housing, etc.)",
      "<strong>Milestone detection:</strong> sobriety count, academic milestones, housing changes = explicit landmark events",
      "<strong>Writeback:</strong> full timeline → RVE profile as enriched life_state context; key events → RVE snapshot as baseline"
    ],
    integrations:["DEEPICKLE","RVE","SHARED"],
    rveLink:"Life timeline feeds RVE profile and context-latest.json export"
  }
];

const CATEGORIES = {
  identity:{label:"IDENTITY",color:"tag-identity"},
  knowledge:{label:"KNOWLEDGE",color:"tag-knowledge"},
  systems:{label:"SYSTEMS",color:"tag-systems"},
  intelligence:{label:"INTELLIGENCE",color:"tag-intelligence"},
  operational:{label:"OPERATIONAL",color:"tag-operational"}
};
const CLASS_NAMES={A:"A·DETERMINISTIC",B:"B·CORPUS AUDIT",C:"C·SOURCE SYNTHESIS",D:"D·DELTA",E:"E·IDEATION",F:"F·COMPARE",G:"G·LONGITUDINAL",H:"H·LENS",I:"I·EVIDENCE LEDGER",J:"J·DRAFT POLISH"};

let currentFilter="all";
let currentCat="all";

function renderCard(t){
  const catDef=CATEGORIES[t.cat];
  return `<div class="target-card" id="card-${t.id}" data-cat="${t.cat}" data-class="${t.missionClass}">
    <div class="card-header" onclick="toggleCard(${t.id})">
      <span class="card-num">${String(t.id).padStart(2,'0')}</span>
      <div class="card-meta">
        <span class="card-title">${t.title}</span>
        <div class="card-tags">
          <span class="tag tag-class">CLASS ${CLASS_NAMES[t.missionClass]||t.missionClass}</span>
          <span class="tag ${catDef.color}">${catDef.label}</span>
        </div>
      </div>
      <span class="card-toggle">▾</span>
    </div>
    <div class="card-body">
      <div class="card-body-inner">
        <div class="body-col">
          <div class="body-section">
            <div class="body-label">Mining Lens</div>
            <div class="body-text">${t.lens}</div>
          </div>
          <div class="body-section">
            <div class="body-label">Phase Pipeline</div>
            <div class="phase-pipeline">
              ${t.phases.map(p=>`<span class="phase${t.keyActive.includes(p)?' active-phase':''}">${p}</span>`).join('<span class="phase-arrow">›</span>')}
            </div>
          </div>
          <div class="body-section">
            <div class="body-label">Output Artifact</div>
            <div class="artifact-badge"><span class="dot"></span>${t.artifact}</div>
          </div>
          <div class="body-section">
            <div class="body-label">System Integrations</div>
            <div class="integration-badges">
              ${t.integrations.map(i=>`<span class="int-badge int-${i.toLowerCase()}">${i}</span>`).join('')}
            </div>
          </div>
          ${t.rveLink?`<div class="body-section"><div class="body-label">RVE Bridge</div><div class="body-text">${t.rveLink}</div></div>`:''}
        </div>
        <div class="body-col">
          <div class="body-section">
            <div class="body-label">FORGE Extraction Operations</div>
            <div class="code-block">${t.extractOps.map(o=>`<span class="kw">→</span> <span class="val">${o}</span>`).join('<br>')}</div>
          </div>
          <div class="body-section">
            <div class="body-label">IN Workflow Optimization</div>
            <ul class="opt-list">${t.inOpt.map(o=>`<li>${o}</li>`).join('')}</ul>
          </div>
        </div>
      </div>
    </div>
  </div>`;
}

function toggleCard(id){
  const el=document.getElementById('card-'+id);
  el.classList.toggle('expanded');
}

const SECTION_LABELS={identity:"IDENTITY & SELF-MODEL",knowledge:"KNOWLEDGE & CAPABILITY",systems:"SYSTEMS & PROJECTS",intelligence:"INTELLIGENCE PRODUCTION",operational:"OPERATIONAL INTELLIGENCE"};

function renderAll(){
  const query=document.getElementById('searchInput').value.toLowerCase();
  const grid=document.getElementById('targetGrid');
  const cats=currentFilter==='all'?['identity','knowledge','systems','intelligence','operational']:[currentFilter];
  let visible=0;
  let html='';
  cats.forEach(cat=>{
    const items=TARGETS.filter(t=>{
      if(t.cat!==cat)return false;
      if(currentCat!=='all'&&t.missionClass!==currentCat)return false;
      if(query&&!`${t.title} ${t.lens} ${t.missionClass} ${t.cat}`.toLowerCase().includes(query))return false;
      return true;
    });
    if(!items.length)return;
    html+=`<div class="section-header"><span class="section-label">${SECTION_LABELS[cat]}</span><div class="section-line"></div></div>`;
    items.forEach(t=>{html+=renderCard(t);visible++;});
  });
  if(!visible)html='<div class="empty-state">NO MATCHING TARGETS FOUND</div>';
  grid.innerHTML=html;
  document.getElementById('visibleCount').textContent=visible;
}

// Filter buttons
document.querySelectorAll('.filter-btn').forEach(btn=>{
  btn.addEventListener('click',()=>{
    document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    currentFilter=btn.dataset.filter;
    renderAll();
  });
});

// Category tabs
document.querySelectorAll('.cat-tab').forEach(tab=>{
  tab.addEventListener('click',()=>{
    document.querySelectorAll('.cat-tab').forEach(t=>t.classList.remove('active'));
    tab.classList.add('active');
    currentCat=tab.dataset.cat;
    renderAll();
  });
});

// Search
document.getElementById('searchInput').addEventListener('input',renderAll);

renderAll();
</script>
</body>
</html>