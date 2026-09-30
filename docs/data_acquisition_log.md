# Data Acquisition Log — v0.2

## Acquired
### Parks
Official Yangpu district park register: 22 records.
Available source attributes include park name, area, park type, subdistrict, address, registry year, star rating and management body.

The original subdistrict label is retained in `subdistrict_raw`. A separate `subdistrict_name` field standardises labels to the current 12-subdistrict naming convention. No geometry has yet been fabricated from addresses; `geometry_status` remains `not_geocoded`.

## Identified but not yet consolidated
- Elderly-care institutions: official district inventory identified.
- Elderly-care capacity: official statistical/planning sources contain bed/building-area information and require entity reconciliation.
- Healthcare: official community health-centre/service-station pages identified.
- Culture: the 12 subdistrict cultural-centre system is evidenced in official district sources.
- Sports: official public sports venue/opening information identified.

## Pending
- Latest authoritative resident population by subdistrict.
- Validated polygons for the 12 subdistricts.

## QA rules
1. Do not substitute migrant population for resident population.
2. Do not infer capacity when the source does not provide it.
3. Keep source labels and standardised labels in separate fields.
4. Do not geocode an address silently; geocoding provenance must be recorded.
5. OSM may supplement spatial geometry/road networks, but must not silently replace authoritative facility inventories.


## v0.3 — Elderly-care layer
- Added the complete 2024 Yangpu District Civil Affairs Bureau inventory: 65 records.
- Contact numbers were intentionally excluded because they are unnecessary for spatial analysis.
- Added a verified extract of 40 planning-capacity records from the official elderly-care facilities layout plan.
- Capacity is explicitly stored as `planned_2025`; it is not treated as observed/licensed 2024 capacity.
- Exact-name matching is used for the first reconciliation pass. Fuzzy/manual matching is deferred to avoid false entity matches.
- Planning documents report 61 institutional facilities and 11,110 planned beds by 2025; this planning universe is not assumed to be identical to the 65-record 2024 operating/service inventory.
