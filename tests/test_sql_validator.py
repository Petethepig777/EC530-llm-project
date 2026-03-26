import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.sql_validator import validate_sql


def test_validate_sql_accepts_valid_select():
    schema_info = {
        "students": {"name": "TEXT", "age": "INTEGER"}
    }

    is_valid, message = validate_sql("SELECT name, age FROM students", schema_info)

    assert is_valid is True


def test_validate_sql_rejects_unknown_table():
    schema_info = {
        "students": {"name": "TEXT", "age": "INTEGER"}
    }

    is_valid, message = validate_sql("SELECT name FROM teachers", schema_info)

    assert is_valid is False
    assert "Unknown table" in message


def test_validate_sql_rejects_unknown_column():
    schema_info = {
        "students": {"name": "TEXT", "age": "INTEGER"}
    }

    is_valid, message = validate_sql("SELECT grade FROM students", schema_info)

    assert is_valid is False
    assert "Unknown column" in message