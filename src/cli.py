from src.db import connect_db, execute_query
from src.csv_loader import load_csv, infer_column_types, insert_rows
from src.schema_manager import (
    get_existing_tables,
    get_table_schema,
    create_table,
    schemas_match,
)
from src.query_service import run_sql_query, run_natural_language_query


def build_schema_info(connection):
    schema_info = {}
    tables = get_existing_tables(connection)

    for table in tables:
        schema_info[table] = get_table_schema(connection, table)

    return schema_info


def handle_load_csv(connection):
    file_path = input("Enter CSV file path: ").strip()
    table_name = input("Enter table name: ").strip()

    try:
        dataframe = load_csv(file_path)
        csv_schema = infer_column_types(dataframe)
        existing_tables = get_existing_tables(connection)

        if table_name in existing_tables:
            db_schema = get_table_schema(connection, table_name)
            if schemas_match(csv_schema, db_schema):
                insert_rows(connection, table_name, dataframe)
                print("Data appended successfully.")
            else:
                print("Schema does not match existing table.")
        else:
            create_table(connection, table_name, csv_schema)
            insert_rows(connection, table_name, dataframe)
            print("Table created and data inserted successfully.")

    except Exception as e:
        print(f"Error loading CSV: {str(e)}")


def handle_list_tables(connection):
    tables = get_existing_tables(connection)

    if not tables:
        print("No tables found.")
        return

    print("Tables:")
    for table in tables:
        print(f"- {table}")


def handle_sql_query(connection):
    sql = input("Enter SQL query: ").strip()
    schema_info = build_schema_info(connection)

    success, result = run_sql_query(connection, sql, schema_info)
    print(result)


def handle_natural_language_query(connection):
    user_query = input("Enter natural language query: ").strip()
    schema_info = build_schema_info(connection)

    success, result = run_natural_language_query(connection, user_query, schema_info)
    print(result)


def run_cli():
    connection = connect_db("project.db")

    while True:
        print("\n=== Data System Menu ===")
        print("1. Load CSV into database")
        print("2. List tables")
        print("3. Run SQL query")
        print("4. Run natural language query")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            handle_load_csv(connection)
        elif choice == "2":
            handle_list_tables(connection)
        elif choice == "3":
            handle_sql_query(connection)
        elif choice == "4":
            handle_natural_language_query(connection)
        elif choice == "5":
            print("Goodbye.")
            connection.close()
            break
        else:
            print("Invalid choice. Please try again.")