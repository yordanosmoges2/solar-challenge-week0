import pandas as pd # type: ignore
import numpy as np # type: ignore
from scipy.stats import zscore # type: ignore

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean dataset: handle missing values and outliers."""
    numeric_cols = ['GHI','DNI','DHI','ModA','ModB','WS','WSgust']
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    z_scores = np.abs(df[numeric_cols].apply(zscore))
    df = df[(z_scores < 3).all(axis=1)]

    print("✅ Cleaned data — removed outliers and filled missing values.")
    return df
