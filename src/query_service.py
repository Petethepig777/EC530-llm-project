from src.db import fetch_all
from src.sql_validator import validate_sql
from src.llm_adapter import generate_sql


def run_sql_query(connection, sql, schema_info):
    is_valid, message = validate_sql(sql, schema_info)
    if not is_valid:
        return False, message

    try:
        rows = fetch_all(connection, sql)
        return True, format_results(rows)
    except Exception as e:
        return False, f"Database error: {str(e)}"


def run_natural_language_query(connection, user_query, schema_info):
    sql = generate_sql(user_query, schema_info)
    return run_sql_query(connection, sql, schema_info)


def format_results(rows):
    if not rows:
        return "No results found."

    lines = []
    for row in rows:
        lines.append(str(row))
    return "\n".join(lines)