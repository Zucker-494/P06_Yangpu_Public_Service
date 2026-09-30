"""
Boundary QA acceptance tests for P06.
Run only after a candidate 12-subdistrict polygon layer has been extracted.
"""
from pathlib import Path
import pandas as pd
import geopandas as gpd

ROOT = Path(__file__).resolve().parents[1]
candidate = ROOT/"data"/"interim"/"yangpu_subdistrict_boundary_candidate.gpkg"
if not candidate.exists():
    raise FileNotFoundError("Candidate boundary layer not found; acquisition/reconciliation must run first.")

gdf = gpd.read_file(candidate)
admin = pd.read_csv(ROOT/"data"/"raw"/"yangpu_subdistrict_admin_reference_2024.csv", dtype={"subdistrict_id":str})
area_ref = pd.read_csv(ROOT/"data"/"raw"/"subdistrict_area_qa_reference_v0.7.csv")

assert len(gdf) == 12, f"Expected 12 polygons, got {len(gdf)}"
assert gdf["subdistrict_name"].nunique() == 12, "Subdistrict names are not unique."
assert set(gdf["subdistrict_name"]) == set(admin["subdistrict_name"]), "Names do not reconcile to authoritative reference."
assert gdf.geometry.notna().all(), "Null geometry found."
assert gdf.is_valid.all(), "Invalid geometry found."

# Project before calculating area. EPSG:32651 is suitable for local metric QA around Shanghai.
metric = gdf.to_crs(32651).copy()
metric["geometry_area_km2"] = metric.area / 1_000_000
check = metric[["subdistrict_name","geometry_area_km2"]].merge(area_ref,on="subdistrict_name",how="left")
check["area_difference_pct"] = (check.geometry_area_km2-check.reference_area_km2)/check.reference_area_km2*100

out=ROOT/"outputs"/"tables"/"boundary_area_qa.csv"
check.to_csv(out,index=False,encoding="utf-8-sig")
print(check.to_string(index=False))
print("Area comparison exported:",out)
print("Topology/union/adjacency review must also be documented before PASS.")
