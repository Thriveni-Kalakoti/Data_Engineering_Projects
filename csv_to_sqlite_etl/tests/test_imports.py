import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


def test_import_etl_module():
    import src.etl
    assert src.etl is not None


def test_import_db_module():
    import src.db
    assert src.db is not None
