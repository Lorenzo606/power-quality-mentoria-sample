from __future__ import annotations

import pandas as pd


def summarize_quality(df: pd.DataFrame) -> dict:
    ts = pd.to_datetime(df["timestamp"], errors="coerce")
    diffs = ts.diff().dt.total_seconds()
    max_gap = diffs.max(skipna=True)

    return {
        "rows": int(len(df)),
        "columns": int(df.shape[1]),
        "null_timestamps": int(ts.isna().sum()),
        "duplicate_timestamps": int(ts.duplicated().sum()),
        "gaps_over_5s": int((diffs > 5).sum()),
        "max_gap_seconds": float(max_gap) if pd.notna(max_gap) else 0.0,
    }
