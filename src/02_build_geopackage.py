"""
Build P06 GeoPackage from approved spatial layers.
This script intentionally refuses to create a misleading 'complete' database when boundary geometry is absent.
"""
from pathlib import Path
import geopandas as gpd

ROOT=Path(__file__).resolve().parents[1]
boundary=ROOT/"data"/"processed"/"boundary_subdistrict.gpkg"
target=ROOT/"p06_yangpu.gpkg"

if not boundary.exists():
    raise FileNotFoundError("Approved boundary_subdistrict geometry is required before building the project GeoPackage.")

gdf=gpd.read_file(boundary)
gdf.to_file(target,layer="boundary_subdistrict",driver="GPKG")
print(f"Created {target} with approved boundary_subdistrict layer.")
