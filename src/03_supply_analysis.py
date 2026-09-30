from pathlib import Path
import pandas as pd
import geopandas as gpd

ROOT = Path(__file__).resolve().parents[1]
GPKG = ROOT / "p06_yangpu.gpkg"

# This script rebuilds the core street-level supply indicators.
# It deliberately excludes sports until its street assignment is independently reconciled.
admin = pd.read_csv(ROOT/"data/raw/yangpu_subdistrict_admin_reference_2024.csv", dtype={"subdistrict_id": str})
pop = pd.read_csv(ROOT/"data/raw/yangpu_subdistrict_resident_population_census2020.csv", dtype={"subdistrict_id": str})
out = admin[["subdistrict_id","subdistrict_name"]].merge(
    pop[["subdistrict_id","population_total"]], on="subdistrict_id", validate="one_to_one"
)

files = {
    "park": "yangpu_parks_official_2021.csv",
    "elderly_care": "yangpu_elderlycare_official_2024.csv",
    "healthcare": "yangpu_community_health_centres_official_v0.4.csv",
    "culture": "yangpu_community_cultural_centres_official_v0.5.csv",
}
for service, filename in files.items():
    d = pd.read_csv(ROOT/"data/raw"/filename)
    count = d.groupby("subdistrict_name").size()
    out[f"{service}_count"] = out["subdistrict_name"].map(count).fillna(0).astype(int)
    out[f"{service}_per_10k"] = out[f"{service}_count"] / out["population_total"] * 10000

park = pd.read_csv(ROOT/"data/raw/yangpu_parks_official_2021.csv")
area = park.groupby("subdistrict_name")["area_m2"].sum()
out["park_area_m2"] = out["subdistrict_name"].map(area).fillna(0)
out["park_area_m2_per_capita"] = out["park_area_m2"] / out["population_total"]

out.to_csv(ROOT/"outputs/tables/analysis_supply_subdistrict_v1.0.csv", index=False, encoding="utf-8-sig")
boundary = gpd.read_file(GPKG, layer="boundary_subdistrict")
geo = boundary.merge(out, on=["subdistrict_id","subdistrict_name"], validate="one_to_one")
geo.to_file(GPKG, layer="analysis_supply", driver="GPKG")
