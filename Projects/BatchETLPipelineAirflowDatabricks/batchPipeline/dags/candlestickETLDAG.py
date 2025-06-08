from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess, os

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="candlestick_etl",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval="@monthly",
    catchup=False,
) as dag:

    download = PythonOperator(
        task_id="download_to_s3",
        python_callable=lambda: subprocess.run(
            ["python", "/opt/airflow/scripts/download_candlestick_data.py"], check=True
        ),
    )

    run_databricks_job = PythonOperator(
        task_id="run_databricks_job",
        python_callable=lambda: subprocess.run(
            [
                "databricks", "jobs", "run-now",
                "--job-id", os.environ["DATABRICKS_JOB_ID"]
            ],
            check=True
        ),
    )

    load_pg = PythonOperator(
        task_id="load_parquet_to_postgres",
        python_callable=lambda: subprocess.run(
            ["python", "/opt/airflow/scripts/load_to_postgres.py"], check=True
        ),
    )

    download >> run_databricks_job >> load_pg
