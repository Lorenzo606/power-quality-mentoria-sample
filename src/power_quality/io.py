from __future__ import annotations

from pathlib import Path
import pandas as pd


def load_sample(csv_path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df["timestamp"] = pd.to_datetime(df["Date"] + " " + df["Time"], errors="coerce")
    df = df.sort_values("timestamp").reset_index(drop=True)
    return df
