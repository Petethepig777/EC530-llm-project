def get_existing_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cursor.fetchall()
    return [row[0] for row in rows]


def get_table_schema(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    rows = cursor.fetchall()

    schema = {}
    for row in rows:
        column_name = row[1]
        column_type = row[2]
        if column_name != "id":
            schema[column_name] = column_type

    return schema


def create_table(connection, table_name, columns):
    cursor = connection.cursor()

    column_defs = ["id INTEGER PRIMARY KEY AUTOINCREMENT"]
    for column_name, column_type in columns.items():
        column_defs.append(f"{column_name} {column_type}")

    sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)});"
    cursor.execute(sql)
    connection.commit()


def schemas_match(csv_schema, db_schema):
    return csv_schema == db_schema


def handle_schema_conflict():
    print("Schema conflict detected.")
    print("Choose one option: overwrite / rename / skip")
    choice = input("Enter choice: ").strip().lower()

    if choice in ["overwrite", "rename", "skip"]:
        return choice

    print("Invalid choice. Defaulting to skip.")
    return "skip"