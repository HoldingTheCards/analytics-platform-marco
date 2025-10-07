
# Roadmap Import – Issues, Labels & Milestones

Diese Anleitung importiert deine Roadmap **als GitHub-Issues** mit Meilensteinen & Labels.

## Repo-Name (Empfehlungen)
**Primär:** `analytics-platform-marco`  
**Alternativen:** `marco-ae-cloud-lab`, `web-analytics-warehouse-gcp-dbt`, `marco-analytics-engineering-portfolio`, `ae-gcp-dbt-powerbi-starter`

**Beschreibung (Vorschlag):**  
_Analytics Engineering Portfolio: BigQuery + dbt (contracts/tests/docs), Orchestration (Airflow/Prefect), Server-side tracking PoC, Data Quality & Power BI Decision Hub._

---
## Voraussetzungen
- GitHub CLI `gh` installiert & angemeldet (`gh auth login`).
- Bash & Python 3.

## Schritte
1. **Repo anlegen**
   ```bash
   export REPO="<owner>/<repo>"   # z. B. deinuser/analytics-platform-marco
   gh repo create "$REPO" --public --confirm
   git clone "https://github.com/$REPO.git"
   cd "$(basename "$REPO")"
   ```
2. **Artefakte ins Repo kopieren & committen**  
   `GitHub_Issues_Import_Roadmap.csv`, `labels.sh`, `milestones.sh`, `create_issues.py`, optional `Roadmap_Checkliste_AE_Cloud_Marco.csv`
3. **Labels & Meilensteine erzeugen**
   ```bash
   export REPO="<owner>/<repo>"
   bash labels.sh
   bash milestones.sh
   ```
4. **Issues anlegen**
   ```bash
   export REPO="<owner>/<repo>"
   export CSV_FILE="./GitHub_Issues_Import_Roadmap.csv"
   python3 create_issues.py
   ```
   *Dry-Run:* `DRY_RUN=1 python3 create_issues.py`

## Optional: Project Board
```bash
gh project create --owner "$(cut -d'/' -f1 <<< "$REPO")" --title "AE+Cloud Roadmap"
```
Filter: `label:Roadmap`
