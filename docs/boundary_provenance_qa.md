# Subdistrict Boundary Provenance and QA — v0.6

## Authoritative semantic reference
The current Yangpu administrative framework contains 12 subdistricts. Names and administrative codes are taken from Shanghai Civil Affairs sources.

Yangpu planning documents explicitly use street administrative boundaries to define the 12 planning units.

## Geometry status
A directly downloadable official polygon dataset for all 12 Yangpu subdistricts has not yet been verified.

Therefore:
- administrative names/codes must remain authoritative;
- any open-source polygon geometry used operationally must be labelled by its actual geometry source;
- no third-party/open polygon may be described as an official boundary;
- geometry must pass QA before analytical use.

## Required geometry QA
1. Exactly 12 unique subdistrict polygons after cleaning.
2. Names/codes reconcile to the authoritative 12-unit reference table.
3. Union is spatially consistent with the Yangpu district extent.
4. No unexplained overlaps or internal gaps.
5. Adjacency is checked against official street descriptions/planning maps where practical.
6. Area values are compared with official subdistrict area descriptions when available.
7. CRS and geometry source/version are recorded.

## Analysis rule
No facility-to-subdistrict spatial join or accessibility aggregation is final until the boundary layer passes this QA.

## v0.7 implementation note
Geofabrik currently publishes regularly updated Shanghai OSM extracts in GeoPackage, Shapefile and PBF formats. Automated large-file retrieval was attempted in the project execution environment but did not complete successfully. No geometry file is therefore claimed as acquired in v0.7.

The repository now contains a fail-loud acquisition entry point (`src/00_acquire_boundary.py`) and QA script (`src/00_boundary_qa.py`). This preserves reproducibility without inventing a successful download.

### Temporal area QA
Area reference values carry a reference year. A historical complete table is retained for coverage, while newer official subdistrict values replace historical values where individually verified. Area mismatch is therefore treated as a reconciliation signal, not an automatic geometry failure.
