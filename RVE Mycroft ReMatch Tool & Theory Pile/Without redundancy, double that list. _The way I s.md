<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Without redundancy, double that list.

The way I see it, ensuring I have all of the always-on stuff that I could need and replacing the system prompt for Gemini with instructions to use these as needed - i don't see that going wrong, right?

Good news and one honest caveat first, then the doubled list.

## The honest caveat: GEMINI.md ≠ system prompt replacement

Telling Gemini "here are all your global tools, use them as needed" in `GEMINI.md` works well **with one real risk**: context bloat. Every token in `GEMINI.md` is loaded into every session, and if you dump 200 tool descriptions into it, you'll bloat context, raise costs, slow responses, and ironically make tool selection *worse* because the model gets overwhelmed.[^1][^2][^3]

The right approach:

- **Global GEMINI.md** (~home dir): short — your identity, communication style, core behavior rules, and the 6–8 always-active tools.
- **Project GEMINI.md** (~project dir): concise — the specific tools, workflows, and constraints for *that project*.
- **`GEMINI_SYSTEM_MD`** env variable: the "nuclear option" — full system prompt override when you need it.[^2]

You can absolutely have everything installed globally. The trick is that Gemini only *needs to know about* what's relevant right now. That said — yes, installing a massive always-on toolkit is correct and encouraged. Here's the doubled list.[^3]

***

## The Complete Always-On Global Toolkit

### 🔧 Shell \& Core Replacements

*(New additions — no repeats from last list)*


| Tool | Replaces | What it does |
| :-- | :-- | :-- |
| **ugrep** | `grep` | Fastest grep alternative; interactive TUI mode with `ug -Q` [^4] |
| **broot** | file nav | Interactive tree browser; navigate, search, preview in one TUI |
| **yazi** | file manager | Full terminal file manager with preview, bulk operations [^4] |
| **duf** | `df` | Modern disk space tool — shows mounted drives beautifully [^5] |
| **gdu** | `du`/`ncdu` | Very fast disk usage analyzer, faster than ncdu [^6] |
| **erdtree** (`et`) | `tree` | Better `tree` command — respects .gitignore, colorized [^5] |
| **choose** | `cut`/`awk` | Human-friendly column selector; `choose 0 3` instead of `awk '{print $1,$4}'` |
| **tre** | `tree` | Fast tree command with editor integration |
| **ouch** | archive tools | Compress/decompress any format (zip, tar, gz, zst) with one command |
| **xh** | `curl`/`httpie` | Fastest HTTP client; httpie-compatible syntax, written in Rust |
| **dog** / **doggo** | `dig` | Modern DNS lookup with colored, structured output [^5] |
| **viddy** | `watch` | Modern `watch` — reruns commands with diff highlighting |


***

### 🧠 Shell Intelligence \& History

| Tool | What it does |
| :-- | :-- |
| **carapace** | Universal shell completion engine — tab-complete nearly any command |
| **navi** | Interactive cheatsheet browser in the terminal; type a keyword, get the command |
| **thefuck** | Auto-corrects the last command you mistyped; hit `fuck` and it fixes it [^7] |
| **pet** | Simple CLI snippet manager — save and recall your own commands |
| **just** | Command runner (like Makefile but readable); define project shortcuts in a `Justfile` |
| **task** (go-task) | Modern Makefile replacement with YAML syntax; great for workflow automation |


***

### 📊 Data, JSON \& Text Processing

| Tool | What it does |
| :-- | :-- |
| **fx** | Interactive JSON viewer and processor — browse JSON like a file tree [^6] |
| **gron** | Makes JSON grep-able: `gron file.json \| grep path` |
| **dasel** | Select/update JSON, YAML, TOML, CSV from CLI — like jq but multi-format |
| **visidata** (`vd`) | Spreadsheet-like TUI for CSV, JSON, SQLite, logs — extremely powerful |
| **q** | Run SQL directly on CSV files: `q "SELECT * FROM file.csv WHERE col > 5"` |
| **pdfgrep** | grep-inside PDF files without converting first |
| **catdoc** | Extract text from .doc/.xls files from CLI |
| **hexyl** | Beautiful hex viewer with colored output |


***

### 🌐 Web, Research \& Media

| Tool | What it does |
| :-- | :-- |
| **yt-dlp** | Download video/audio from 1000+ sites; the gold standard [^8] |
| **gallery-dl** | Download image galleries from Imgur, Reddit, Patreon, Instagram, etc. [^9] |
| **monolith** | Save a complete webpage as a single HTML file (inline CSS, JS, images) |
| **readability-cli** | Extract clean article text from a URL — like browser reader mode |
| **w3m** / **lynx** | Text-based web browsers; scriptable, pipe-friendly |
| **aria2** | High-speed multi-protocol downloader (HTTP, BitTorrent, Metalink) — faster than wget |
| **rclone** | Cloud storage CLI — sync to/from Google Drive, S3, Dropbox, etc. |
| **newsboat** | Terminal RSS reader with scriptable feed processing |


***

### 🔐 OSINT \& Recon

| Tool | What it does |
| :-- | :-- |
| **theHarvester** | Gather emails, subdomains, IPs from Google/Bing/LinkedIn/Shodan/VirusTotal [^10][^11] |
| **recon-ng** | Modular web recon framework; hundreds of modules, API-integrated [^12][^13] |
| **SpiderFoot** | Automated OSINT automation across 200+ sources [^12][^14] |
| **exiftool** | Extract metadata from images, PDFs, Office docs — geolocation, timestamps, authors |
| **DNSDumpster** (CLI/API) | DNS record mapping, subdomain discovery |
| **shodan** (CLI) | Search Shodan from terminal — exposed IPs, services, vulnerabilities |
| **sublist3r** | Fast subdomain enumeration using multiple search engines |
| **waybackurls** | Pull all URLs for a domain from the Wayback Machine |
| **gitleaks** | Scan git repos for leaked secrets/credentials |


***

### 📝 Writing, Docs \& Knowledge

| Tool | What it does |
| :-- | :-- |
| **glow** | Render markdown beautifully in the terminal (already listed — key for your workflow) |
| **mdcat** | Another terminal markdown renderer — lighter than glow |
| **vale** | Prose linting — checks writing style, consistency, tone |
| **aspell** / **hunspell** | CLI spellcheckers |
| **wc** / **wordcounttools** | Word/character count; useful for content targets |
| **translate-shell** (`trans`) | Translate text via Google/DeepL/etc. from CLI |
| **wtf** / **tldr** / **tealdeer** | Instant man-page summaries — `tldr curl` gives you the 5 most useful examples [^15][^16] |
| **cheat** | Create and view your own cheatsheets per command |


***

### 🤖 AI \& LLM (Global Tier)

| Tool | What it does |
| :-- | :-- |
| **llm** (Simon Willison) | Query OpenAI, Gemini, Anthropic, Ollama from CLI; pipe text through models |
| **aichat** | Multi-model REPL + shell integration; role-based prompting |
| **fabric** | AI augmentation framework with pre-built "patterns" (summarize, extract wisdom, etc.) — highly relevant for your knowledge distillation workflow |
| **sgpt** | Natural language → shell commands; `sgpt "find all PDFs modified this week"` |
| **mods** | Pipe CLI output through an LLM — `cat log.txt \| mods "summarize errors"` |


***

### ⚙️ Process, System \& Monitoring

| Tool | What it does |
| :-- | :-- |
| **hyperfine** | CLI benchmarking — time any command with statistics |
| **gping** | Graphical ping in the terminal — shows latency over time as a chart |
| **bandwhich** | Real-time network bandwidth by process |
| **ctop** | Container-aware `top` — like htop but shows Docker containers |
| **sysz** | `fzf`-powered systemd service manager |
| **lnav** | Log file navigator — tail, search, highlight multiple log files simultaneously |
| **tailspin** | Colorize and highlight any log file automatically |


***

### 🔑 Security \& Crypto

| Tool | What it does |
| :-- | :-- |
| **age** | Simple, modern file encryption — better than GPG for most uses |
| **sops** | Encrypt secrets in YAML/JSON/ENV files; works with age or GPG |
| **trufflehog** | Scan for secrets leaked in git history, S3, etc. |
| **nuclei** | Fast vulnerability scanner using community templates |
| **ffuf** | Web fuzzer — brute-force directories, parameters, subdomains |


***

### 📦 Package \& Version Management

| Tool | What it does |
| :-- | :-- |
| **mise** | Universal version manager — replaces pyenv + nvm + rbenv in one tool [^17] |
| **uv** | Ultra-fast Python package manager (Rust-based); already in list but worth emphasizing |
| **topgrade** | Update everything at once — runs apt, cargo, pipx, npm, gem, brew, etc. |
| **chezmoi** | Dotfile manager — keeps your shell configs synced across machines |


***

## The GEMINI.md strategy

Now that you have this full list, here is how to handle it intelligently with Gemini:

- **Home `~/.gemini/GEMINI.md`**: List only the ~15 core always-active tools in a short table. Describe your identity, tone preferences, and default behavior rules. Keep it under ~300 lines.[^3]
- **`~/.gemini/tool-registry.md`** (separate file, NOT auto-loaded): Your full master tool list — a reference *you* consult to decide what to add to project contexts.
- **Project `./GEMINI.md`**: Pull in only the bands relevant to that project. A research project gets `ripgrep`, `llm`, `fabric`, `yt-dlp`, `glow`. A news scraping project adds `theHarvester`, `newsboat`, `Firecrawl`.

This keeps the always-loaded context lean and sharp while your full arsenal is always installed and ready to reference.[^2][^3]

***

## Master Install Script (WSL)

```bash
# Rust-based tools (via cargo)
cargo install bat eza zoxide bottom dust procs sd xsv erdtree ouch choose hyperfine \
  hexyl ripgrep fd-find broot viddy bandwhich

# Apt
sudo apt install -y fzf jq yq tmux pandoc nmap mtr aria2 w3m lynx pdfgrep \
  aspell translate-shell lnav thefuck age ffuf whois curl wget

# pipx (Python global tools - isolated envs)
pipx install yt-dlp
pipx install gallery-dl
pipx install theharvester
pipx install recon-ng
pipx install spiderfoot
pipx install llm
pipx install fabric
pipx install sgpt
pipx install mods
pipx install vale
pipx install gitleaks
pipx install trufflehog

# Go tools
go install github.com/jesseduffield/lazygit@latest
go install github.com/sxyazi/yazi@latest
go install github.com/tomnomnom/waybackurls@latest
go install github.com/hakluke/hakrawler@latest

# Shell enhancements
curl -sS https://starship.rs/install.sh | sh
cargo install tealdeer && tldr --update
```

<span style="display:none">[^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31]</span>

<div align="center">⁂</div>

[^1]: https://github.com/google-gemini/gemini-cli/discussions/7432

[^2]: https://danicat.dev/posts/20250715-gemini-cli-system-prompt/

[^3]: https://www.youtube.com/watch?v=U-8zgiSKSr4

[^4]: https://community.tmpdir.org/t/new-alternatives-to-well-known-unix-linux-terminal-commands/392

[^5]: https://notes.billmill.org/computer_usage/cli_tips_and_tools/modern_unix_tool_list.html

[^6]: https://news.ycombinator.com/item?id=41292835

[^7]: https://tech.yahoo.com/computing/articles/ve-written-python-years-install-113016197.html

[^8]: https://pypi.org/project/yt-dlp/

[^9]: https://www.plug.org.nz/wp-content/uploads/2023/11/yt-dlp-gallery-dl.pdf

[^10]: https://www.hackthebox.com/blog/10-osint-tools

[^11]: https://shadowdragon.io/blog/best-osint-tools/

[^12]: https://lampyre.io/blog/15-best-osint-tools-in-2025/

[^13]: https://plextrac.com/the-most-popular-penetration-testing-tools-this-year/

[^14]: https://www.reddit.com/r/hacking/comments/vr7bah/what_are_your_preferred_osint_tools/

[^15]: https://www.hostzealot.com/blog/about-solutions/13-cli-tools-every-developer-should-master-in-2025

[^16]: https://www.youtube.com/watch?v=mvWYdrn7m2c

[^17]: https://www.git-tower.com/blog/7-cli-tools-every-developer-should-install

[^18]: https://www.reddit.com/r/commandline/comments/1jniqsy/essential_clitui_tools_for_developers/

[^19]: https://dev.to/0xkoji/17-essential-cli-tools-to-boost-developer-productivity-2o9e

[^20]: https://linuxconfig.org/modern-cli-tools-time-to-forget-ls-and-cat

[^21]: https://www.linkedin.com/posts/lunguflorin_13-best-linux-cli-tools-for-developers-in-activity-7295581374890012672-vtZz

[^22]: https://github.com/pypa/pipx

[^23]: https://www.youtube.com/watch?v=PWqVVLuUdTs

[^24]: https://www.reddit.com/r/Python/comments/yegk2m/share_your_pipx_list/

[^25]: https://www.boxpiper.com/posts/top-best-tools-for-developer

[^26]: https://www.youtube.com/watch?v=0sNnssilAEQ

[^27]: https://www.pynetlabs.com/osint-tools/

[^28]: https://www.youtube.com/watch?v=FGixDiPM2FU

[^29]: https://www.webasha.com/blog/what-are-the-best-osint-tools-for-cybersecurity-and-investigations-in-2026

[^30]: https://github.com/mikf/gallery-dl/issues/8911

[^31]: https://news.ycombinator.com/item?id=26561211

