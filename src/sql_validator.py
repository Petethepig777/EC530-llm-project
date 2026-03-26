import re


def is_select_query(sql):
    return sql.strip().lower().startswith("select")


def extract_table_names(sql):
    matches = re.findall(r"\bfrom\s+([a-zA-Z_][a-zA-Z0-9_]*)", sql, re.IGNORECASE)
    join_matches = re.findall(r"\bjoin\s+([a-zA-Z_][a-zA-Z0-9_]*)", sql, re.IGNORECASE)
    return list(set(matches + join_matches))


def extract_column_names(sql):
    match = re.search(r"select\s+(.*?)\s+from\b", sql, re.IGNORECASE | re.DOTALL)
    if not match:
        return []

    column_text = match.group(1).strip()

    if column_text == "*":
        return ["*"]

    columns = [col.strip() for col in column_text.split(",")]
    cleaned_columns = []

    for col in columns:
        col = re.sub(r"\bas\s+\w+$", "", col, flags=re.IGNORECASE).strip()
        if "." in col:
            col = col.split(".")[-1].strip()
        cleaned_columns.append(col)

    return cleaned_columns


def validate_sql(sql, schema_info):
    if not is_select_query(sql):
        return False, "Only SELECT queries are allowed."

    table_names = extract_table_names(sql)
    if not table_names:
        return False, "Query must reference at least one table."

    for table in table_names:
        if table not in schema_info:
            return False, f"Unknown table: {table}"

    column_names = extract_column_names(sql)

    if column_names != ["*"]:
        valid_columns = set()
        for table in table_names:
            valid_columns.update(schema_info[table].keys())
            valid_columns.add("id")

        for column in column_names:
            if "(" in column or ")" in column:
                continue
            if column not in valid_columns:
                return False, f"Unknown column: {column}"

    return True, "SQL is valid."