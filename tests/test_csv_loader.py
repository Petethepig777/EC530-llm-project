import pandas as pd
from src.csv_loader import infer_column_types


def test_infer_column_types():
    df = pd.DataFrame({
        "age": [20, 21],
        "score": [95.5, 88.0],
        "name": ["Alice", "Bob"]
    })

    result = infer_column_types(df)

    assert result["age"] == "INTEGER"
    assert result["score"] == "REAL"
    assert result["name"] == "TEXT"