import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import sqlite3
from src.schema_manager import create_table, get_existing_tables, get_table_schema, schemas_match


def test_create_table_and_get_schema():
    connection = sqlite3.connect(":memory:")
    columns = {"name": "TEXT", "age": "INTEGER"}

    create_table(connection, "students", columns)

    tables = get_existing_tables(connection)
    schema = get_table_schema(connection, "students")

    assert "students" in tables
    assert schema == columns


def test_schemas_match():
    schema1 = {"name": "TEXT", "age": "INTEGER"}
    schema2 = {"name": "TEXT", "age": "INTEGER"}
    schema3 = {"name": "TEXT", "age": "REAL"}

    assert schemas_match(schema1, schema2) is True
    assert schemas_match(schema1, schema3) is False