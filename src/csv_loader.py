import pandas as pd


def load_csv(file_path):
    return pd.read_csv(file_path)


def infer_column_types(dataframe):
    column_types = {}

    for column in dataframe.columns:
        if pd.api.types.is_integer_dtype(dataframe[column]):
            column_types[column] = "INTEGER"
        elif pd.api.types.is_float_dtype(dataframe[column]):
            column_types[column] = "REAL"
        else:
            column_types[column] = "TEXT"

    return column_types


def insert_rows(connection, table_name, dataframe):
    cursor = connection.cursor()

    columns = list(dataframe.columns)
    column_names = ", ".join(columns)
    placeholders = ", ".join(["?"] * len(columns))

    sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"

    for _, row in dataframe.iterrows():
        cursor.execute(sql, tuple(row))

    connection.commit()