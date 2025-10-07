# Migration auf Cloud (später)

- **DuckDB → BigQuery**: `dbt-duckdb` gegen `dbt-bigquery` tauschen, `profiles.yml` anpassen.
- **Prefect (lokal) → Airflow/Composer**: Flows als Airflow DAG nachbauen; dieselben dbt Commands.
- **Landing (Parquet) → Objekt-Storage**: Writer austauschen (GCS, S3), Pfade in Staging-Models anpassen.
