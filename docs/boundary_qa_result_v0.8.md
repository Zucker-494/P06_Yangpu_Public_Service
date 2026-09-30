# Boundary QA Result — v0.8

## Source separation
- Administrative names/codes: Shanghai Civil Affairs authoritative reference.
- Operational polygon geometry: Geofabrik Shanghai OSM extract, snapshot 2026-09-28.
- OSM geometry is not represented as an official government polygon.

## Extraction
All 12 authoritative Yangpu subdistrict names were found in `gis_osm_adminareas_a_free`.
All 12 are represented as `admin_level8`.

## Geometry QA
- Polygon count: 12 — PASS
- Unique authoritative names: 12 — PASS
- Geometry validity: all valid — PASS
- Sum of subdistrict polygon areas: 60.507920 km²
- Union area: 60.507920 km²
- OSM Yangpu district polygon area: 60.507920 km²
- Internal overlap: -0.0000000000 km²
- Street union outside district: 0.0000000000 km²
- District area uncovered by street union: 0.0000000000 km²

Topology and district-union consistency therefore PASS.

## Area-reference warning
Area references are time-sensitive and may use different administrative/measurement conventions.
In particular, Daqiao's operational OSM geometry is approximately 4.375 km², while the 2024 official subdistrict profile reports 3.99 km².
This is retained as a QA warning rather than resolved by altering geometry, because the 12-subdistrict union exactly matches the OSM Yangpu district polygon.

## Approval
The layer is approved as the project's operational subdistrict geometry for subsequent reproducible spatial analysis, subject to the provenance and limitation statements above.
