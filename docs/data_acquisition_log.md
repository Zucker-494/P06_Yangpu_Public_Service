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
