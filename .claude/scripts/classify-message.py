#!/usr/bin/env python3
"""Classify user messages and inject routing hints for Claude."""
import json
import sys
import re

def classify(prompt: str) -> list[str]:
    p = prompt.lower()
    signals = []

    # Decision signals
    if any(w in p for w in ["decided", "decision", "we chose", "agreed to", "let's go with", "the call is", "we're going with"]):
        signals.append("DECISION detected — consider creating a Decision Record in work/active/ and logging in work/Index.md Decisions Log")

    # Incident signals
    if any(w in p for w in ["incident", "outage", "down", "pagerduty", "severity", "p0", "p1", "p2", "sev1", "sev2", "postmortem", "rca"]):
        signals.append("INCIDENT detected — consider using /incident-capture or creating an incident note in work/incidents/")

    # 1-on-1 signals
    if any(w in p for w in ["1:1", "1-on-1", "one on one", "1on1", "catch up with", "sync with"]):
        signals.append("1:1 CONTENT detected — consider creating a 1-on-1 note in work/1-1/ and updating the person note in org/people/")

    # Win/achievement signals
    if any(w in p for w in ["shipped", "launched", "completed", "achieved", "won", "promoted", "kudos", "shoutout", "great feedback", "recognized"]):
        signals.append("WIN detected — consider adding to perf/Brag Doc.md with a link to the evidence note")

    # Architecture/design signals
    if any(w in p for w in ["architecture", "system design", "rfc", "tech spec", "trade-off", "design doc", "adr"]):
        signals.append("ARCHITECTURE discussion — consider creating a reference note in reference/ or a decision record")

    # Person signals (mentions of someone by context)
    if any(w in p for w in ["told me", "said that", "feedback from", "met with", "talked to", "spoke with", "mentioned that"]):
        signals.append("PERSON CONTEXT detected — consider updating the relevant person note in org/people/ and linking from the conversation note")

    # Project update signals
    if any(w in p for w in ["project update", "sprint", "milestone", "shipped feature", "released", "deployed"]):
        signals.append("PROJECT UPDATE detected — consider updating the active work note in work/active/ and checking if wins should go to brag doc")

    return signals

def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    prompt = input_data.get("prompt", "")
    if not prompt:
        sys.exit(0)

    signals = classify(prompt)

    if signals:
        hints = "\n".join(f"- {s}" for s in signals)
        output = {
            "hookSpecificOutput": {
                "additionalContext": (
                    "Content classification hints (act on these if the user's message contains relevant info):\n"
                    + hints
                    + "\n\nRemember: use proper templates, add [[wikilinks]], follow CLAUDE.md conventions."
                )
            }
        }
        json.dump(output, sys.stdout)

    sys.exit(0)

if __name__ == "__main__":
    main()
