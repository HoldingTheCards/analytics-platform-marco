# analytics-platform-marco-free

**Kostenfreie Roadmap-Umsetzung** für Analytics Engineering – komplett **ohne Cloud-Kosten**.  
Stack: **dbt + DuckDB (lokal)**, **Prefect (OSS)**, **FastAPI Collector (lokal)**, **Great Expectations (optional)**, **Streamlit/Power BI Desktop**.

> ⚠️ Demo-/synthetische Daten nur. Keine Secrets/Prod-Daten im Repo.

## Warum DuckDB?
- Läuft **embedded** (eine `.duckdb`-Datei) → 0€ Betriebskosten.
- Sehr schnell für Analytics-Workloads, perfekt mit **dbt-duckdb**.
- Später leicht auf BQ/Snowflake/PG migrierbar (Modelle wiederverwendbar).

## Architektur (kostenfrei)
```mermaid
flowchart LR
  A[FastAPI Collector (lokal)] --> L[(local landing: parquet/ndjson)]
  L --> S[dbt stg (DuckDB)]
  S --> C[dbt core models]
  C --> G[Gold marts (DuckDB)]
  G --> D1[Streamlit Dashboard]
  G --> D2[Power BI Desktop]
  subgraph Orchestration (OSS)
    P[Prefect: Flows, Schedules, Alerts (local)]
  end
  P -.-> A
  P -.-> S
  P -.-> C
```

## Quickstart
```bash
# 1) (optional) venv aktivieren
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Abhängigkeiten installieren
pip install -r requirements.txt

# 3) Synthetische Events erzeugen
python scripts/generate_synthetic_events.py --out data/events.csv --rows 10000

# 4) dbt: compile/build (DuckDB)
#  - Profile nutzt dbt-duckdb und schreibt analytics.duckdb nach ./data
dbt deps || true
dbt debug || true
dbt build

# 5) Prefect Flow (lokal) laufen lassen
python orchestration/prefect_flow.py

# 6) Dashboard (frei wählbar)
# Streamlit (kostenfrei, lokal):
streamlit run dashboards/streamlit_app.py
# oder Power BI Desktop (Windows, kostenfrei): PBIX auf ./data/analytics.duckdb legen
```

## Zero-Cost Map (Cloud → Frei)
| Thema | Cloud (kostenpflichtig) | Frei/OSS (hier) |
|---|---|---|
| DWH | BigQuery | **DuckDB** (embedded Datei) |
| Orchestrierung | Composer/Airflow Cloud | **Prefect OSS** (lokal) |
| Ingestion/Landing | GCS/BQ Landing | **Parquet/NDJSON** im `./data` Ordner |
| Streaming | Pub/Sub | **lokal**: Datei-Append / (optional) `watchdog` |
| Data Quality | Cloud DQ | **dbt tests** (+ optional **Great Expectations**) |
| BI | Power BI Service | **Power BI Desktop** **oder** **Streamlit** |
| CI | GitHub Actions (kostenfrei public) | **GitHub Actions** (hier: dbt-duckdb & sqlfluff) |

## Migration später
- Adapter tauschen (duckdb → bigquery/snowflake/postgres), Modelle bleiben.
- Orchestrierung: Prefect → Airflow/Composer problemlos möglich.
- Landing: parquet → objektstorage/Cloud-Table Writer.

## Lizenz
MIT
