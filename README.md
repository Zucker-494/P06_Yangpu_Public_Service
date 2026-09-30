# P06 — Yangpu Public Service Assessment and Spatial Decision Support

## Status
P06-05: Data Acquisition & Preparation — v1.3.1 (pedestrian topology repair)

## Project type
Independent portfolio project simulating a Chinese GIS/planning horizontal-project workflow.

## Study area
Yangpu District, Shanghai. Primary reporting units: 12 subdistricts.

## Core question
Where are public-service provision, accessibility, and demand–supply mismatches located, and what type of intervention should be prioritised?

## Current implementation
Python / GeoPandas + GeoPackage + QGIS. No new software is required during the thesis-submission period.

## Workflow
Raw data → standardisation → spatial integration → supply analysis → accessibility analysis → gap diagnosis → decision-support outputs.

## Important
This is a simulated consultancy workflow, not a commissioned project. Official/authoritative data are preferred. Missing client-type datasets remain explicit data requirements rather than being silently replaced by weak proxies.


## Data acquisition status
The first authoritative facility layer has been acquired: the official Yangpu district park register (22 records). Additional official sources for elderly care, healthcare, culture and sports have been identified and are being consolidated before spatial analysis begins.

- Elderly-care layer: 65 official 2024 institution/service-home records added; planning capacity is maintained as a separate, typed source.

- Healthcare core layer: all 12 community health service centres consolidated from official Yangpu sources.
- The officially confirmed 66 service stations are retained as a separate pending secondary layer to avoid mixing facility tiers or inconsistent source years.

- Culture: all 12 subdistrict community cultural-centre institutions confirmed; unresolved address/version issues are explicitly flagged.
- Sports: 20 high-confidence public/community sports-facility records added with facility-tier semantics.
- Visual acceptance requirements are now formally recorded in `docs/visual_specification.md`.

- Demand baseline: complete authoritative 2020 Census resident population for all 12 subdistricts (1,242,600 residents).
- Temporal control: 2024 district resident population (1,199,700) retained without synthetic street-level redistribution.
- Administrative reference: current 12-subdistrict names and codes frozen from Shanghai Civil Affairs.
- Boundary geometry remains provenance-controlled and must pass QA before final spatial joins.

- Spatialisation pipeline now separates authoritative administrative semantics from operational geometry provenance.
- Added time-aware official area QA references and fail-loud boundary acquisition/QA scripts.
- No polygon or GeoPackage is falsely claimed as complete: spatial database construction is gated by boundary QA.

- Operational geometry: all 12 current Yangpu subdistrict polygons extracted from the 2026-09-28 Geofabrik Shanghai OSM snapshot.
- Boundary topology and district-union QA passed.
- `p06_yangpu.gpkg` now contains approved subdistrict boundaries, the census-baseline population polygon layer, and district context geometry.

- Facility spatialisation has begun using reproducible OSM feature matching and subdistrict consistency checks; unresolved official facilities remain unlocated rather than receiving guessed coordinates.

- `analysis_supply` is now implemented for parks, elderly care, healthcare, and culture using authoritative facility inventories and the frozen 2020 Census population baseline.
- Facility geometry evidence is explicitly classified A/B/C; only A-grade points are eligible for future network accessibility analysis.
- Sports street-level supply and all accessibility indicators remain deferred rather than being estimated from incomplete coordinates.

- Added a formal limitations/future-work register linking each data constraint to its analytical consequence, mitigation, and upgrade path.
- Added an indicator interpretation registry so temporal scope, readiness, and inferential limits travel with the analysis.
- Added transparent district-relative supply diagnostics. Median-based labels are exploratory screening only and are not interpreted as official adequacy standards.
- Final service-gap classification remains pending accessibility evidence.

- Audited which supply indicators genuinely warrant maps versus charts/tables.
- Selected park area per resident and elderly-care facilities per 10,000 residents as primary supply-map candidates.
- Kept healthcare and culture rates as supporting evidence because their variation is dominated by the one-centre-per-subdistrict structure.
- Added a preliminary contrast chart and a formal visual-evidence selection registry.

- Extracted a Yangpu pedestrian-network candidate from the 2026-09-29 OSM PBF with a 1 km boundary buffer.
- Added network QA and explicit pedestrian filtering rules.
- Added a conservative 80% A-grade facility-geometry gate for category-wide accessibility modelling.
- Accessibility remains intentionally deferred because facility-location completeness, rather than network availability, is currently the binding constraint.

- Reconstructed pedestrian topology by noding linework at geometric intersections.
- Added full noded and largest-component routing-core layers.
- Connectivity QA now evaluates both node share and network-length share.
- Planar noding's potential to over-connect grade-separated crossings is explicitly retained as a routing limitation.
