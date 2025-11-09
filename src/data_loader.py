import pandas as pd # type: ignore
from pathlib import Path

def load_data(file_path: str) -> pd.DataFrame:
    """Load dataset into a pandas DataFrame."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    df = pd.read_csv(path)
    print(f"✅ Loaded {len(df)} rows from {file_path}")
    return df
