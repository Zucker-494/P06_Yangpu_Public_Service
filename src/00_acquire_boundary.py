"""
P06 v0.7 — acquire/extract operational Yangpu subdistrict geometry.

Design rules
------------
1. Administrative names/codes come from the authoritative project reference table.
2. Geometry provenance must remain OSM/Geofabrik (or another actual source); never relabel as official.
3. No final spatial join is allowed until geometry passes QA.
4. Download is intentionally separated from analysis so a failed network request cannot silently alter results.

Expected input
--------------
A current Geofabrik Shanghai free GeoPackage, manually downloaded if automated retrieval is unavailable:
https://download.geofabrik.de/asia/china/

Place the archive/extracted GPKG in data/raw/external/osm/.

Workflow
--------
- inspect available boundary/multipolygon layer names;
- filter candidate administrative boundaries by Yangpu's 12 authoritative names;
- normalize names using data/raw/yangpu_subdistrict_admin_reference_2024.csv;
- reproject to an appropriate projected CRS for area QA;
- calculate geometry area;
- compare against data/raw/subdistrict_area_qa_reference_v0.7.csv;
- check polygon count, uniqueness, validity, overlaps/gaps and Yangpu union;
- export ONLY a passed layer to p06_yangpu.gpkg as boundary_subdistrict.

This script is a controlled acquisition/QA entry point. It must fail loudly rather than fabricate missing geometry.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
EXT = RAW / "external" / "osm"
EXT.mkdir(parents=True, exist_ok=True)

gpkg_files = list(EXT.glob("*.gpkg"))
if not gpkg_files:
    raise FileNotFoundError(
        "No Geofabrik Shanghai GeoPackage found. "
        "Download the current Shanghai free GPKG and place it in data/raw/external/osm/. "
        "Do not substitute an untracked boundary file."
    )

try:
    import geopandas as gpd
    import fiona
except ImportError as e:
    raise RuntimeError("Existing GeoPandas/Fiona environment is required.") from e

source = gpkg_files[0]
layers = fiona.listlayers(source)
print("Available layers:", layers)

# Layer schema differs by Geofabrik release; do not hard-code a guessed layer name.
candidate_layers = [x for x in layers if "admin" in x.lower() or "boundary" in x.lower()]
if not candidate_layers:
    raise RuntimeError("No obvious administrative/boundary layer found; inspect layer schemas before continuing.")

print("Candidate boundary layers:", candidate_layers)
print("Next step: inspect candidate schema and filter the authoritative 12 Yangpu subdistrict names.")
print("No geometry has been exported yet.")
