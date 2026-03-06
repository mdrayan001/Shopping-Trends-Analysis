"""
visualizer.py
-------------
Reusable plotting functions for shopping trends EDA.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

OUTPUT_DIR = "../outputs/figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_distribution(df: pd.DataFrame, column: str, color: str = "steelblue") -> None:
    """Plot and save a histogram for a numeric column."""
    plt.figure(figsize=(8, 4))
    plt.hist(df[column].dropna(), bins=25, color=color, edgecolor="white")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/dist_{column.replace(' ', '_')}.png", dpi=150)
    plt.show()


def plot_category_counts(df: pd.DataFrame, column: str) -> None:
    """Plot and save a bar chart of value counts for a categorical column."""
    plt.figure(figsize=(10, 5))
    df[column].value_counts().plot(kind="bar", color="mediumseagreen", edgecolor="white")
    plt.title(f"Count by {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/count_{column.replace(' ', '_')}.png", dpi=150)
    plt.show()


def plot_group_mean(df: pd.DataFrame, group_col: str, value_col: str) -> None:
    """Plot mean of value_col grouped by group_col."""
    plt.figure(figsize=(8, 4))
    df.groupby(group_col)[value_col].mean().sort_values(ascending=False).plot(
        kind="bar", color="coral", edgecolor="white"
    )
    plt.title(f"Average {value_col} by {group_col}")
    plt.xlabel(group_col)
    plt.ylabel(f"Avg {value_col}")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/mean_{group_col}_vs_{value_col}.png".replace(" ", "_"), dpi=150)
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Plot correlation heatmap for numeric columns."""
    plt.figure(figsize=(10, 7))
    corr = df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/correlation_heatmap.png", dpi=150)
    plt.show()
