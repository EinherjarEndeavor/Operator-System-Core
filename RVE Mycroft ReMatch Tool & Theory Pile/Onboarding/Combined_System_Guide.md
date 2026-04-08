# Combined System Guide: Tool Arsenal, Setup, and Research

## Table of Contents
1. [Summary of Actions](#summary-of-actions)
2. [Tool Arsenal (Categorized & Deduplicated)](#tool-arsenal)
    - [AI & LLM Frameworks / Runtimes](#ai-llm-frameworks)
    - [Intelligence & OSINT](#intelligence-osint)
    - [Data Science & Analytics](#data-analytics)
    - [Content Extraction & Conversion](#content-extraction)
    - [Automation & Browser Control](#automation-browser)
    - [Network & Security](#network-security)
    - [Infrastructure & DevOps](#infrastructure-devops)
    - [Multimedia Processing](#multimedia-processing)
    - [Knowledge Management & Knowledge Base](#knowledge-management)
3. [System Setup Summaries](#system-setup-summaries)
    - [Architecture Blueprint](#architecture-blueprint)
    - [Phase-Based Setup Guide](#phase-based-setup-guide)
4. [Deep Research Summaries](#deep-research-summaries)
    - [Research Methodologies (STORM, SATs, DRACO)](#research-methodologies)
    - [Extraction Taxonomies](#extraction-taxonomies)
    - [Workflow Blueprint](#research-workflow-blueprint)
5. [Fringe Experimentation Protocol](#fringe-experimentation)

---

## Summary of Actions
This document is a consolidation of 37 Markdown files from the `Onboarding` directory. The following actions were performed:
- **Extraction:** Analyzed all files to identify tools, system setup instructions, and research methodologies.
- **Deduplication:** Merged duplicate tool mentions and selected the most descriptive entries.
- **Categorization:** Grouped hundreds of tools into logical domains for easier navigation.
- **Synthesis:** Summarized complex multi-phase setup guides and elite research blueprints into a coherent reference.
- **Refinement:** Applied the "MegaMan X" equipment metaphor to the system architecture as requested in the source documents.

---

## Tool Arsenal

### AI & LLM Frameworks / Runtimes <a name="ai-llm-frameworks"></a>
- **Gemini CLI**: Primary operator surface for interacting with Google's Gemini models.
- **Ollama**: Local runner for Llama 3, Mistral, and other open-weight models.
- **LangChain**: Framework for building LLM applications through composability.
- **LlamaIndex**: Data framework for connecting LLMs to custom data sources.
- **CrewAI**: Role-based multi-agent orchestration framework.
- **AutoGen**: Microsoft's framework for multi-agent conversation systems.
- **Semantic Kernel**: Microsoft SDK for integrating AI with existing code.
- **LiteLLM**: Unified API gateway for 100+ LLMs.
- **MemGPT**: Memory management system for unbounded context in LLMs.
- **Maestro-Gemini**: Orchestrator for specialist Gemini sub-agents.
- **PydanticAI**: Type-safe agent building using Pydantic.
- **OpenRouter**: Unified API for accessing multiple frontier models.

### Intelligence & OSINT <a name="intelligence-osint"></a>
- **Sherlock**: Username footprinting across 350+ sites.
- **Maigret**: Recursive username dossier generation.
- **GHunt**: Google Account investigation and footprinting.
- **SpiderFoot**: Modular automation for OSINT gathering.
- **theHarvester**: E-mail, subdomain, and names harvesting.
- **Holehe**: Email-based account discovery without notifying the user.
- **Recon-ng**: Full-stack web reconnaissance framework.
- **Amass**: In-depth DNS enumeration and attack surface mapping.
- **Shodan CLI**: Internet-wide device discovery.
- **IntelX**: Search engine for the darknet and data breaches.
- **Maltego**: Graph-based link analysis and data integration.

### Data Science & Analytics <a name="data-analytics"></a>
- **Pandas**: The industry standard for tabular data manipulation.
- **Polars**: Blazing fast DataFrame library written in Rust.
- **DuckDB**: In-process SQL OLAP database for complex queries on flat files.
- **VisiData**: CLI-based interactive dataset explorer.
- **CSVKit**: Suite of tools for converting and manipulating CSVs.
- **Numpy / SciPy**: Fundamental libraries for numerical and scientific computing.
- **Scikit-Learn**: Machine learning library for predictive modeling.
- **Matplotlib / Seaborn / Plotly**: Visualization libraries for static and interactive charts.
- **Yellowbrick**: Visual analysis and diagnostic tools for machine learning.

### Content Extraction & Conversion <a name="content-extraction"></a>
- **Trafilatura**: Advanced web text and metadata extraction.
- **MarkItDown**: Microsoft's tool for converting various formats to Markdown.
- **Tesseract OCR**: High-quality optical character recognition engine.
- **Pandoc**: The "universal document converter" for Markdown, PDF, Docx, etc.
- **Unstructured**: Document partitioning and preprocessing for RAG.
- **PyMuPDF (fitz)**: High-performance PDF parsing and rendering.
- **Tabula-py**: Specialized tool for extracting tables from PDFs.
- **Docling**: High-fidelity document parsing for AI applications.
- **Newspaper4k**: News article metadata parsing and extraction.

### Automation & Browser Control <a name="automation-browser"></a>
- **Playwright**: Modern headless browser automation for Chromium, Firefox, and WebKit.
- **Puppeteer**: Node.js library for controlling headless Chrome.
- **Selenium**: The classic browser automation framework.
- **Open Interpreter**: Natural language interface for your computer's terminal.
- **Aider**: AI pair programmer that works directly in the terminal.
- **Actiona**: Cross-platform automation tool for GUI tasks.

### Network & Security <a name="network-security"></a>
- **Nmap**: Network exploration and security auditing tool.
- **Wireshark / Tshark**: Network protocol analyzers.
- **Tor Browser**: Primary tool for anonymous browsing and darknet access.
- **Signal**: Encrypted messaging for secure communication.
- **VeraCrypt**: Hidden volume disk encryption.
- **TruffleHog**: Secrets and API key harvesting/scanning.
- **Vault (HashiCorp)**: Secure management of secrets and API keys.
- **GnuPG (GPG)**: Complete implementation of the OpenPGP standard.

### Infrastructure & DevOps <a name="infrastructure-devops"></a>
- **Docker / Podman**: Containerization for isolating agent environments.
- **Terraform**: Infrastructure as Code for managing servers and resources.
- **Ansible**: System configuration and automation.
- **Tailscale**: Zero-config VPN for connecting remote agents.
- **Temporal**: Durable execution framework for long-running tasks.
- **N8n**: Low-code workflow automation for connecting apps.
- **LocalStack**: Local AWS cloud simulation for testing.

### Multimedia Processing <a name="multimedia-processing"></a>
- **FFmpeg**: The Swiss Army knife for audio and video transcoding.
- **ImageMagick**: CLI-based image manipulation and batch processing.
- **MoviePy**: Scriptable video editing in Python.
- **Pillow (PIL)**: Python imaging library for image cleaning and enhancement.
- **WhisperX / Faster-Whisper**: High-speed speech-to-text with word-level timestamps.
- **Spleeter**: AI-based source separation (isolating voices from noise).

### Knowledge Management & Knowledge Base <a name="knowledge-management"></a>
- **Obsidian**: Markdown-based personal knowledge base (the "Truth Base").
- **Neo4j**: Graph database for mapping complex entity relationships.
- **ChromaDB / Qdrant / Weaviate**: Vector databases for semantic search and RAG.
- **mq**: Advanced CLI tool for structural querying of Markdown files.

---

## System Setup Summaries

### Architecture Blueprint <a name="architecture-blueprint"></a>
The system is modeled after the **MegaMan X equipment model**, defining specific roles for various software components:
- **Helmet (Orchestration):** Temporal for durable execution; Gemini CLI + Maestro for interactive tasks.
- **Chest (Memory):** Obsidian Vault (Truth Base) + Mem0 for semantic memory.
- **Arms (Workers):** Specialist Gemini agents and sub-agents.
- **Weapons (Tools):** MCP servers, project-scoped scripts, and global CLI tools.
- **Boots (Scheduling):** Docker environments and Temporal schedules.
- **Cape/Aura (Observability):** Logs, retrospective notes, and project status artifacts.

### Phase-Based Setup Guide <a name="phase-based-setup-guide"></a>
The setup follows a parallel track for **WSL (Linux)** and **PowerShell (Windows)**:
1. **Foundation:** Create a mirrored `~/Operator` root directory.
2. **Package Managers:** Install `uv`, `mise`, `pipx`, and `winget`.
3. **CLI Base:** Install "always-on" tools (`rg`, `fd`, `fzf`, `bat`, `jq`, `pandoc`, `glow`).
4. **Gemini CLI:** Global install of the primary operator interface.
5. **Vault Skeleton:** Initialize the Obsidian-first folder structure (`Arsenal`, `Axioms`, `Projects`, `Re`, `Journey`).
6. **Project Scoping:** Implement `GEMINI.md` and `tool_use.md` logic to prevent context bloat by lazy-loading tools only when needed.

---

## Deep Research Summaries

### Research Methodologies <a name="research-methodologies"></a>
- **STORM (Stanford):** Uses perspective-guided questioning and outline hardening *before* synthesis to produce Wikipedia-quality reports.
- **SATs (Structured Analytic Techniques):** Intelligence tradecraft including *Analysis of Competing Hypotheses (ACH)* and *Key Assumptions Check (KAC)* to eliminate bias.
- **DRACO Benchmark:** Evaluation framework focused on accuracy, breadth, and citation quality.

### Extraction Taxonomies <a name="extraction-taxonomies"></a>
The system extracts specific high-value units from source material:
- **Axioms / Primals:** Smallest useful action-intel units.
- **Principles / Heuristics:** Reusable mental models and decision rules.
- **Mechanisms:** Causal chains explaining *how* something works.
- **Tensions:** Points of contradiction or conflicting evidence.

### Research Workflow Blueprint <a name="research-workflow-blueprint"></a>
1. **Frame:** Decompose query into a question tree and perspective map.
2. **Scout:** Breadth-first evidence gathering to populate a *Claim Registry*.
3. **Harden:** Validate outline against gathered evidence; identify gaps.
4. **Depth:** Targeted deep dives into identified gaps and contradictions.
5. **Synthesize:** Evidence-to-artifact generation focusing on explanatory power.
6. **Red Team:** Adversarial critique of conclusions and assumptions.

---

## Fringe Experimentation Protocol <a name="fringe-experimentation"></a>
A specialized system for biohacking and performance optimization:
- **Component Analysis:** Identifying stressors and physiological targets.
- **Measurement:** Tracking energy, energy, mood, and objective biomarkers.
- **Ejection Criteria:** Hard thresholds for stopping experiments (e.g., Vitals spikes, sleep disruption).
- **Research Query Trajectory:** Mapping mechanisms (e.g., "nicotine + straw = hypoxic adaptation") to find mechanistic support.
