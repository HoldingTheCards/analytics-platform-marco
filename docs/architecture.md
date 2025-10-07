# Architecture & SLAs

- **Freshness (batch)**: < 4h
- **Streaming P95**: < 2 min (optional phase)
- **Data Validity**: > 99% on consent=granted
- **Costs**: Tracked via BQ query plan & slot usage

```mermaid
graph TD
  C[Collector] --> L[Landing (BQ)]
  L --> S[Staging (dbt)]
  S --> G[Gold Marts]
  G --> BI[Power BI]
  S --> DOCS[dbt Docs]
  subgraph Control
    ORCH[Airflow/Prefect]
  end
  ORCH --> L
  ORCH --> S
  ORCH --> DOCS
```
