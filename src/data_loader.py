"""
data_loader.py
--------------
Utility for loading the shopping trends dataset.
"""

import pandas as pd
import os


def load_data(filepath: str = "../data/shopping_trends.csv") -> pd.DataFrame:
    """
    Load the shopping trends CSV into a DataFrame.

    Args:
        filepath: Path to the CSV file.

    Returns:
        pd.DataFrame: Raw dataset.

    Raises:
        FileNotFoundError: If the CSV is not found at the given path.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Dataset not found at '{filepath}'.\n"
            "Please download it from Kaggle and place it in the data/ folder:\n"
            "https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset"
        )

    df = pd.read_csv(filepath)
    print(f"✅ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")
    return df
