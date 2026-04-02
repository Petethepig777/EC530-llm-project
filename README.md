# EC530 LLM Project

A lightweight local CSV data query system that supports both SQL queries and natural language queries.

## Features
- Load CSV files into SQLite
- List tables
- Run direct SQL queries
- Run natural language queries
- Safe SQL validation
- Command-line interface

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the system:

python main.py

## Example Flow
1. Load CSV
2. List tables
3. Run SQL query
4. Run natural language query

Example natural language query:

show all students

## Files
- src/db.py
- src/csv_loader.py
- src/schema_manager.py
- src/sql_validator.py
- src/query_service.py
- src/cli.py
- main.py

## How to Run Tests

In the terminal, run:

```bash
pytest
```

To run a specific test file:

```bash
pytest tests/test_query_service.py
```