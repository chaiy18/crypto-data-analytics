from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append("/home/chai/crypto-data-analytics") 

from pipelines.batch_pipeline import run_pipeline

default_args = {
    "owner": "chai",
    "retries": 1
}

with DAG(
    dag_id="crypto-data-analytics",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
    tags=["crypto", "pyspark", "finstream"]
) as dag:

    run_pipeline_task = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_pipeline
    )