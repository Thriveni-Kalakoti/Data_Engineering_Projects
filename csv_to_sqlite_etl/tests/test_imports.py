def test_import_etl_module():
    import src.etl
    assert src.etl is not None


def test_import_db_module():
    import src.db
    assert src.db is not None
