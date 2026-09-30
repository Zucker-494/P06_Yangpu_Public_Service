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


## v0.4 — Primary healthcare core layer
- Added all 12 Yangpu community health service centres as the high-confidence core healthcare layer.
- Centre and station tiers are explicitly separated; downstream accessibility analysis must not count them as equivalent facility units.
- Official Yangpu sources confirm a district-wide `12 + 66` primary-care network (12 centres and 66 service stations).
- The 66-station secondary layer is not yet populated because a complete, same-period official station-name/address inventory has not been consolidated.
- Licensed bed capacity is populated only where a specific official source supports it; capacity reference dates are retained because values are not all from the same year.
- No coordinates have been fabricated from postal addresses. Geocoding remains a separate auditable step.


## v0.5 — Culture and sports layers
### Culture
- Confirmed the institutional network of 12 subdistrict community cultural activity centres.
- The 2024 municipal evaluation identified 4 Yangpu centres as demonstration centres and the other 8 as grade-1 centres.
- Address values are populated only when individually supported by official district material.
- Multiple official addresses for some centres are treated as a reconciliation issue (main centre / branch / relocation), not silently collapsed into one location.

### Sports
- Added 20 high-confidence public/community sports-facility records from official Yangpu public-opening information.
- Facility tiers are retained (`public_sports_venue`, `community_fitness_centre`, `community_fitness_station`, `public_ball_court`) so later supply analysis does not count unlike facilities as equivalent.
- Co-located culture/sports services are retained as legitimate multi-service sites rather than deduplicated away.

### Visualization acceptance condition
Final cartography must use deliberate visual hierarchy, high-contrast continuous ramps where appropriate, designed point size/stroke/transparency, subdued contextual layers, readable legends/labels at README or paper-column scale, and analytically distinct map purposes. A Neighborhood × Service Gap Heatmap remains a required non-map analytical output.
