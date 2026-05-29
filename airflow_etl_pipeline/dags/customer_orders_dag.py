from datetime import datetime, timedelta
from pathlib import Path
import sys

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import PythonOperator

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.etl_tasks import run_etl_pipeline


default_args = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="customer_orders_etl_pipeline",
    description="ETL pipeline for processing customer orders data",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["data-engineering", "etl", "orders"],
) as dag:

    start = EmptyOperator(task_id="start")

    run_customer_orders_etl = PythonOperator(
        task_id="run_customer_orders_etl",
        python_callable=run_etl_pipeline,
    )

    end = EmptyOperator(task_id="end")

    start >> run_customer_orders_etl >> end