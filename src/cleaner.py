"""
cleaner.py
----------
Data cleaning pipeline for the shopping trends dataset.
"""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full cleaning pipeline:
    - Remove duplicates
    - Impute missing numeric values with median
    - Impute missing categorical values with mode

    Args:
        df: Raw DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    original_len = len(df)

    # Drop duplicates
    df = df.drop_duplicates()
    print(f"Removed {original_len - len(df)} duplicate rows.")

    # Impute numeric columns
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        missing = df[col].isnull().sum()
        if missing > 0:
            df[col].fillna(df[col].median(), inplace=True)
            print(f"  Imputed {missing} missing values in '{col}' with median.")

    # Impute categorical columns
    cat_cols = df.select_dtypes(include="object").columns
    for col in cat_cols:
        missing = df[col].isnull().sum()
        if missing > 0:
            df[col].fillna(df[col].mode()[0], inplace=True)
            print(f"  Imputed {missing} missing values in '{col}' with mode.")

    print(f"✅ Cleaning complete. Final shape: {df.shape}")
    return df
