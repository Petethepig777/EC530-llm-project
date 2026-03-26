from src.llm_adapter import generate_sql


def test_generate_sql_returns_select_statement():
    schema_info = {
        "students": {"name": "TEXT", "age": "INTEGER"}
    }

    sql = generate_sql("show all students", schema_info)

    assert sql.lower().startswith("select")