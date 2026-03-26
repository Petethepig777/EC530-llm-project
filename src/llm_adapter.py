def generate_sql(user_query, schema_info):
    query = user_query.strip().lower()

    if len(schema_info) == 0:
        return "SELECT 1"

    first_table = list(schema_info.keys())[0]

    if "all" in query or "show" in query or "list" in query:
        return f"SELECT * FROM {first_table}"

    return f"SELECT * FROM {first_table} LIMIT 5"