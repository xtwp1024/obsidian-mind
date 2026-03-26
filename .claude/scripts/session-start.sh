#!/bin/bash
set -euo pipefail
cd "$CLAUDE_PROJECT_DIR"

# Persist vault path for the session
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export VAULT_PATH=$CLAUDE_PROJECT_DIR" >> "$CLAUDE_ENV_FILE"
fi

# Incremental QMD re-index (fast, non-blocking if qmd not installed)
qmd update 2>/dev/null || true

# Build context summary
echo "## Session Context"
echo ""
echo "### Date"
echo "$(date +%Y-%m-%d) ($(date +%A))"
echo ""

echo "### North Star (current goals)"
if command -v obsidian &>/dev/null; then
  obsidian read file="North Star" 2>/dev/null | head -30 || cat brain/North\ Star.md 2>/dev/null | head -30
else
  cat brain/North\ Star.md 2>/dev/null | head -30
fi
echo ""

echo "### Recent Changes (last 48h)"
git log --oneline --since="48 hours ago" --no-merges 2>/dev/null | head -15 || echo "(no git history)"
echo ""

echo "### Open Tasks"
if command -v obsidian &>/dev/null; then
  obsidian tasks daily todo 2>/dev/null | head -10 || echo "(none or CLI unavailable)"
else
  echo "(Obsidian CLI not available)"
fi
echo ""

echo "### Active Work"
ls work/active/*.md 2>/dev/null | sed 's|work/active/||;s|\.md$||' | head -10 || echo "(none)"
echo ""

echo "### Vault File Listing"
find . -name "*.md" -not -path "./.obsidian/*" -not -path "./thinking/*" -not -path "./.claude/*" | sort
