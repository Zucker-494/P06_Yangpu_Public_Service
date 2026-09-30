# Facility Spatialisation — v0.9

## Method
Facility coordinates are not fabricated from addresses. The first spatialisation pass uses the user-supplied Geofabrik Shanghai OSM snapshot (2026-09-28) as a reproducible candidate geometry source.

Matching procedure:
1. Build a pool of named OSM POI/building/land-use/natural features inside Yangpu.
2. Normalise facility names for candidate comparison.
3. Accept unique normalised-name matches or high-confidence fuzzy-name candidates.
4. Validate candidate points against the authoritative-name operational subdistrict polygons.
5. Reject candidates whose spatial subdistrict conflicts with the facility's recorded subdistrict.
6. Retain all unmatched records explicitly for later resolution.

## Coverage
| facility_type   |   source_records |   approved_osm_geometry |   unresolved |   coverage_pct |
|:----------------|-----------------:|------------------------:|-------------:|---------------:|
| park            |               21 |                      14 |            7 |           66.7 |
| elderly_care    |               65 |                       3 |           62 |            4.6 |
| healthcare      |               12 |                       6 |            6 |           50   |
| culture         |               12 |                       5 |            7 |           41.7 |
| sports          |               20 |                       0 |           20 |            0   |

## Interpretation
This is a conservative first pass. Coverage is not treated as a quality score: an unresolved official facility remains valid tabular data but is not assigned a guessed coordinate.

## Next step
Resolve remaining facilities through auditable address-based geocoding and/or additional official spatial references, then rerun subdistrict validation before accessibility analysis.
