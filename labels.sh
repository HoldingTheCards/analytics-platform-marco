#!/usr/bin/env bash
set -euo pipefail
if [[ -z "${REPO:-}" ]]; then echo "Please export REPO=<owner>/<repo>"; exit 1; fi
# Requires: GitHub CLI (gh)
echo "Creating labels in $REPO ..."
gh label create "Roadmap" --repo "$REPO" --color "0E8A16" --description "Roadmap tasks" || true
gh label create "Prio:P1" --repo "$REPO" --color "B60205" --description "Priority P1" || true
gh label create "Prio:P2" --repo "$REPO" --color "D93F0B" --description "Priority P2" || true
gh label create "Prio:P3" --repo "$REPO" --color "FBCA04" --description "Priority P3" || true
gh label create "Phase:Apr 2026" --repo "$REPO" --color "1D76DB" --description "Phase Apr 2026" || true
gh label create "Phase:Dez 2025" --repo "$REPO" --color "1D76DB" --description "Phase Dez 2025" || true
gh label create "Phase:Fast‑Start (12 Wochen)" --repo "$REPO" --color "1D76DB" --description "Phase Fast‑Start (12 Wochen)" || true
gh label create "Phase:Feb 2026" --repo "$REPO" --color "1D76DB" --description "Phase Feb 2026" || true
gh label create "Phase:Jan 2026" --repo "$REPO" --color "1D76DB" --description "Phase Jan 2026" || true
gh label create "Phase:Jun 2026" --repo "$REPO" --color "1D76DB" --description "Phase Jun 2026" || true
gh label create "Phase:Mai 2026" --repo "$REPO" --color "1D76DB" --description "Phase Mai 2026" || true
gh label create "Phase:Mrz 2026" --repo "$REPO" --color "1D76DB" --description "Phase Mrz 2026" || true
gh label create "Phase:Nov 2025" --repo "$REPO" --color "1D76DB" --description "Phase Nov 2025" || true
gh label create "Phase:Okt 2025" --repo "$REPO" --color "1D76DB" --description "Phase Okt 2025" || true