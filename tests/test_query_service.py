import sqlite3
from src.schema_manager import create_table
from src.query_service import run_sql_query


def test_run_sql_query_success():
    connection = sqlite3.connect(":memory:")
    create_table(connection, "students", {"name": "TEXT", "age": "INTEGER"})
    connection.execute("INSERT INTO students (name, age) VALUES ('Alice', 20)")
    connection.commit()

    schema_info = {"students": {"name": "TEXT", "age": "INTEGER"}}
    success, result = run_sql_query(connection, "SELECT name, age FROM students", schema_info)

    assert success is True
    assert "Alice" in result


def test_run_sql_query_reject_non_select():
    connection = sqlite3.connect(":memory:")
    schema_info = {}

    success, result = run_sql_query(connection, "DROP TABLE students", schema_info)

    assert success is False
    assert "Only SELECT queries are allowed." in result