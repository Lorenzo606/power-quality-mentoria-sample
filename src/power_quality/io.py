from __future__ import annotations

from pathlib import Path
import pandas as pd


def load_sample(csv_path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    elif {"Date", "Time"}.issubset(df.columns):
        df["timestamp"] = pd.to_datetime(df["Date"] + " " + df["Time"], errors="coerce")
    else:
        raise ValueError(
            "No se pudo construir `timestamp`: el CSV debe incluir una columna `timestamp` "
            "o las columnas `Date` y `Time`."
        )

    df = df.sort_values("timestamp").reset_index(drop=True)
    return df
