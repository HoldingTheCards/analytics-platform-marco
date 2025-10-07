from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "marco",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

def say(msg):
    print(msg)

with DAG(
    dag_id="demo_analytics_pipeline",
    start_date=datetime(2025, 10, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
    tags=["demo","roadmap"]
) as dag:
    ingest = PythonOperator(task_id="ingest", python_callable=say, op_args=["Ingest synthetic events"])
    build  = PythonOperator(task_id="dbt_build", python_callable=say, op_args=["Run dbt build (placeholder)"])
    docs   = PythonOperator(task_id="publish_docs", python_callable=say, op_args=["Publish docs (placeholder)"])

    ingest >> build >> docs
