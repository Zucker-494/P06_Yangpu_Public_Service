"""P06 v1.5 gap diagnosis.

Implements the transparent 2x2 relative diagnostic used in the delivered v1.5 outputs.
Inputs are analysis_supply and outputs/tables/network_accessibility_by_subdistrict_v1.4.csv.
Parks remain accessibility-pending and are not assigned a joint gap type.
"""
from pathlib import Path
import pandas as pd
import geopandas as gpd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
GPKG = ROOT / "p06_yangpu.gpkg"

def classify(supply_class, accessibility_class):
    if supply_class == "high" and accessibility_class == "high":
        return "broadly_adequate"
    if supply_class == "high" and accessibility_class == "low":
        return "spatial_configuration_gap"
    if supply_class == "low" and accessibility_class == "high":
        return "supply_capacity_pressure"
    return "combined_gap"

def main():
    supply = gpd.read_file(GPKG, layer="analysis_supply")
    acc = pd.read_csv(ROOT / "outputs/tables/network_accessibility_by_subdistrict_v1.4.csv")
    rate_map = {
        "healthcare": "healthcare_per_10k",
        "elderly_care": "elderly_care_per_10k",
        "culture": "culture_per_10k",
    }
    rows = []
    for typ, col in rate_map.items():
        d = supply[["subdistrict_name", col]].rename(columns={col:"supply_indicator"})
        a = acc.loc[acc.facility_type.eq(typ),
                    ["subdistrict_name","network_coverage_15min_pct"]]
        d = d.merge(a, on="subdistrict_name", how="left")
        smed = d.supply_indicator.median()
        amed = d.network_coverage_15min_pct.median()
        d["supply_class"] = np.where(d.supply_indicator >= smed, "high", "low")
        d["accessibility_class"] = np.where(d.network_coverage_15min_pct >= amed, "high", "low")
        d["gap_type"] = [classify(s,a) for s,a in zip(d.supply_class,d.accessibility_class)]
        d["facility_type"] = typ
        rows.append(d)
    # Sports and parks require the audited v1.5 handling documented in
    # docs/gap_diagnosis_methodology_v1.5.md.
    pd.concat(rows, ignore_index=True).to_csv(
        ROOT / "outputs/tables/recomputed_core_gap_diagnosis.csv",
        index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    main()
