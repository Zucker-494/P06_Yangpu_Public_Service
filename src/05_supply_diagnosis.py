from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT/"outputs/tables/analysis_supply_subdistrict_v1.0.csv")

indicators = [
    "park_per_10k",
    "park_area_m2_per_capita",
    "elderly_care_per_10k",
    "healthcare_per_10k",
    "culture_per_10k",
]

out = df[["subdistrict_id","subdistrict_name","population_total"]].copy()
for indicator in indicators:
    median = df[indicator].median()
    out[indicator] = df[indicator]
    out[indicator + "_relative_supply"] = np.where(
        df[indicator] < median, "below_median",
        np.where(df[indicator] > median, "above_median", "at_median")
    )

out.to_csv(ROOT/"outputs/tables/supply_diagnostic_subdistrict_v1.1.csv",
           index=False, encoding="utf-8-sig")
