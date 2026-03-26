# System Architecture

## Components

### 1. CSV Loader
- Reads CSV files
- Prepares data for insertion into database

### 2. Schema Manager
- Detects existing tables
- Compares schema
- Creates or updates tables

### 3. Query Service
- Central controller
- Receives user requests
- Calls validator and database

### 4. SQL Validator
- Ensures only safe queries (SELECT)
- Checks tables and columns

### 5. LLM Adapter
- Converts natural language to SQL
- Does NOT execute SQL

### 6. CLI
- User interface
- Sends requests to Query Service

### 7. Database (SQLite)
- Stores data

## Module APIs

### csv_loader.py
- load_csv(file_path)
- infer_column_types(dataframe)
- insert_rows(connection, table_name, dataframe)

### schema_manager.py
- get_existing_tables(connection)
- get_table_schema(connection, table_name)
- create_table(connection, table_name, columns)
- schemas_match(csv_schema, db_schema)

### query_service.py
- run_sql_query(connection, sql)
- run_natural_language_query(connection, user_query, schema_info)
- format_results(rows)

### sql_validator.py
- is_select_query(sql)
- extract_table_names(sql)
- extract_column_names(sql)
- validate_sql(sql, schema_info)

### llm_adapter.py
- generate_sql(user_query, schema_info)

### db.py
- connect_db(db_path)
- execute_query(connection, sql)
- fetch_all(connection, sql)

### cli.py
- run_cli()