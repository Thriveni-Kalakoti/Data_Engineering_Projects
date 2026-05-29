import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "dags"))

from customer_orders_dag import dag


def test_customer_orders_dag_imports_successfully():
    assert dag.dag_id == "customer_orders_etl_pipeline"


def test_customer_orders_dag_has_expected_tasks():
    task_ids = list(dag.task_ids)

    assert "start" in task_ids
    assert "run_customer_orders_etl" in task_ids
    assert "end" in task_ids