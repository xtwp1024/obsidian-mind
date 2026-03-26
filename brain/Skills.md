---
description: "Vault-specific workflows and slash commands — reusable patterns for review prep, project tracking, and vault maintenance"
tags:
  - brain
  - index
---

# Skills

Custom slash commands, subagents, and reusable workflows. Defined in `.claude/commands/` and `.claude/agents/`.

## Slash Commands

### Daily Workflow

| Command | Purpose |
|---------|---------|
| `/standup` | Morning kickoff — load context, review yesterday, surface tasks, identify priorities |
| `/dump` | Freeform capture — dump anything, gets routed to the right notes automatically |
| `/wrap-up` | Full session review — verify notes, indexes, links, suggest improvements. Auto-triggered on "wrap up". |

### Capture & Documentation

| Command | Purpose |
|---------|---------|
| `/capture-1on1` | Capture 1:1 meeting transcript into structured vault note with quotes, action items, DM context |
| `/incident-capture` | Capture incident from Slack channels/DMs into structured vault notes — timeline, people, analysis, brag entry |
| `/slack-scan` | Deep scan Slack channels/DMs for evidence — extracts timestamped touchpoints, organizes by context |

### Performance & Review

| Command | Purpose |
|---------|---------|
| `/peer-scan` | Deep scan a peer's GitHub PRs for review prep — produces structured analysis saved to `perf/evidence/` |
| `/review-brief` | Generate review brief (manager or peer version) from vault data |

### Vault Maintenance

| Command | Purpose |
|---------|---------|
| `/vault-audit` | Deep structural audit — indexes, frontmatter, links, Bases, folder placement, stale context |
| `/project-archive` | Move completed project from `work/active/` to `work/archive/YYYY/`, update all indexes |

## Subagents

| Agent | Purpose | Invoked by |
|-------|---------|------------|
| `brag-spotter` | Proactively finds uncaptured wins and competency gaps | `/wrap-up` |
| `context-loader` | Loads all vault context about a person, project, incident, or concept | Direct — "load context on X" |
| `cross-linker` | Finds missing wikilinks, orphans, broken backlinks across the vault | `/vault-audit` |
| `people-profiler` | Bulk create/update person notes from Slack profiles | `/incident-capture` |
| `review-prep` | Aggregates all performance evidence for a given review period | `/review-brief` |
| `slack-archaeologist` | Full Slack reconstruction — reads every message, thread, profile, produces unified timeline | `/incident-capture` |
| `vault-librarian` | Deep vault maintenance — orphan detection, broken links, frontmatter validation, stale notes | `/vault-audit` |

Subagents run in isolated context windows via `.claude/agents/`. They don't pollute the main conversation.

## Hooks

| Hook | When | What |
|------|------|------|
| SessionStart | On startup/resume | QMD re-index, inject North Star, active work, recent changes, tasks, file listing |
| UserPromptSubmit | Every message | Classify content (decision, incident, 1:1, win, architecture, person, project update) and inject routing hints |
| PreToolUse (Write/Edit) | Before file writes | Validate frontmatter, check for wikilinks, verify folder placement |
| PreCompact | Before context compaction | Back up session transcript to `thinking/session-logs/` |
| Stop | End of session | Checklist: archive, update indexes, check orphans |

## Semantic Search (QMD)

If QMD is installed (`npm install -g @tobilu/qmd`), the vault has semantic search:

- `qmd query "..."` — hybrid BM25 + vector + LLM reranking (best quality)
- `qmd search "..."` — fast BM25 keyword search
- `qmd vsearch "..."` — semantic vector search (exploratory)
- `qmd update && qmd embed` — refresh index after bulk changes

SessionStart hook runs `qmd update` automatically. See `.claude/skills/qmd/SKILL.md` for full reference.

## Workflow: Full Review Cycle Prep

1. **`/review-brief manager`** — generate the manager context transfer doc
2. **`/review-brief peers`** — generate the peer context transfer doc
3. **`/peer-scan`** (parallel, one per peer) — deep scan each peer's PRs
4. **`/slack-scan`** — scan relevant channels for your own evidence + peer context
5. **`/capture-1on1`** — capture the review 1:1 with your manager
6. **`/vault-audit`** — tidy up after all the new data

## Workflow: Project Ramp-Up

1. **`/slack-scan`** — scan project channels for history and decisions
2. **`/peer-scan`** (if needed) — understand what teammates have already built
3. Create work note from gathered context
4. **`/vault-audit`** — ensure everything links properly
