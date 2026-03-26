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