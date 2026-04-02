from src.db import fetch_all
from src.sql_validator import validate_sql
from src.llm_adapter import generate_sql


def log_error(message):
    with open("error_log.txt", "a") as file:
        file.write(message + "\n")


def run_sql_query(connection, sql, schema_info):
    is_valid, message = validate_sql(sql, schema_info)
    if not is_valid:
        log_error(f"Validation error: {message} | SQL: {sql}")
        return False, message

    try:
        rows = fetch_all(connection, sql)
        return True, format_results(rows)
    except Exception as e:
        log_error(f"Database error: {str(e)} | SQL: {sql}")
        return False, f"Database error: {str(e)}"


def run_natural_language_query(connection, user_query, schema_info):
    try:
        sql = generate_sql(user_query, schema_info)
        return run_sql_query(connection, sql, schema_info)
    except Exception as e:
        log_error(f"LLM/query generation error: {str(e)} | User query: {user_query}")
        return False, f"Query generation error: {str(e)}"


def format_results(rows):
    if not rows:
        return "No results found."

    lines = []
    for row in rows:
        lines.append(str(row))
    return "\n".join(lines)