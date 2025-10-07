#!/usr/bin/env bash
set -euo pipefail
if [[ -z "${REPO:-}" ]]; then echo "Please export REPO=<owner>/<repo>"; exit 1; fi
# Requires: GitHub CLI (gh)
echo "Creating milestones in $REPO ..."
gh issue milestone create "Okt 2025 – Fundament & Setup" -d "Milestone for roadmap phase: Okt 2025 – Fundament & Setup" -D "2025-10-31" --repo "$REPO" || true
gh issue milestone create "Nov 2025 – Modellierung & dbt" -d "Milestone for roadmap phase: Nov 2025 – Modellierung & dbt" -D "2025-11-30" --repo "$REPO" || true
gh issue milestone create "Dez 2025 – Orchestrierung & Data Quality" -d "Milestone for roadmap phase: Dez 2025 – Orchestrierung & Data Quality" -D "2025-12-29" --repo "$REPO" || true
gh issue milestone create "Jan 2026 – Privacy & Server-Side Tracking (PoC)" -d "Milestone for roadmap phase: Jan 2026 – Privacy & Server-Side Tracking (PoC)" -D "2026-01-25" --repo "$REPO" || true
gh issue milestone create "Feb 2026 – CI/CD, Kosten, Sicherheit" -d "Milestone for roadmap phase: Feb 2026 – CI/CD, Kosten, Sicherheit" -D "2026-02-22" --repo "$REPO" || true
gh issue milestone create "Mrz 2026 – BI Enablement (Power BI)" -d "Milestone for roadmap phase: Mrz 2026 – BI Enablement (Power BI)" -D "2026-03-29" --repo "$REPO" || true
gh issue milestone create "Apr 2026 – Zertifizierung & Systemdesign" -d "Milestone for roadmap phase: Apr 2026 – Zertifizierung & Systemdesign" -D "2026-04-28" --repo "$REPO" || true
gh issue milestone create "Mai 2026 – Streaming/Realtime & Observability" -d "Milestone for roadmap phase: Mai 2026 – Streaming/Realtime & Observability" -D "2026-05-20" --repo "$REPO" || true
gh issue milestone create "Jun 2026 – Portfolio & Bewerbung" -d "Milestone for roadmap phase: Jun 2026 – Portfolio & Bewerbung" -D "2026-06-25" --repo "$REPO" || true
gh issue milestone create "Fast‑Start (12 Wochen)" -d "Milestone for roadmap phase: Fast‑Start (12 Wochen)" -D "2025-12-31" --repo "$REPO" || true