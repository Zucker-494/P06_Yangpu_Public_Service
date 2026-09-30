# P06 — Yangpu Public Service Assessment and Spatial Decision Support

## Status
**P06-06: Final Analysis & Portfolio Delivery — v2.0**

Core analytical workflow complete: multi-source data integration → structured spatial database → supply assessment → pedestrian-network accessibility → demand–supply gap diagnosis → intervention-oriented outputs → final cartographic delivery.

Park accessibility remains an explicitly documented enhancement because parks require entrance-based rather than single-point accessibility modelling.

## Project type
Independent portfolio project simulating a Chinese GIS/planning horizontal-project workflow.  
**This is not a commissioned government project.**

## Study area
Yangpu District, Shanghai, using the current 12 subdistricts as the primary reporting units.

## Decision question
**Where are public-service provision, accessibility, and demand–supply mismatches located, and what type of intervention should be prioritised?**

The project is designed around a planning workflow rather than a single GIS technique. It separates supply shortage from spatial-access problems so that the same map does not automatically imply the same intervention.

## Service categories
- Healthcare
- Elderly care
- Culture
- Sports
- Parks / green space

## Analytical framework

### 1. Supply
Facility inventories are standardized by service category and linked to the 2020 Census subdistrict population baseline. Core indicators include facilities per 10,000 residents and, for parks, park area per resident. Capacity is retained only where an authoritative source provides it; missing capacity is not imputed.

### 2. Pedestrian accessibility
The OSM pedestrian network was planar-noded and checked for connectivity before routing. Validated facilities are connected to the routing core using nearest-edge projection rather than nearest-node snapping.

Accessibility is reported as the share of modeled pedestrian-network length within 5, 10 and 15 minutes of the nearest facility. A baseline walking speed of 1.2 m/s is used.

**This is network-length coverage, not population coverage.** Authoritative population is available only at subdistrict level, so the project does not fabricate fine-scale resident exposure.

### 3. Demand–supply diagnosis
Healthcare, elderly care, culture and sports are classified using a transparent 2×2 relative diagnostic:

| Supply | Accessibility | Diagnostic | Intervention interpretation |
|---|---|---|---|
| High | High | Broadly adequate | Maintain and monitor |
| High | Low | Spatial configuration gap | Redistribute access points / spatially targeted provision |
| Low | High | Supply/capacity pressure | Expand provision or capacity |
| Low | Low | Combined gap | Combined supply and spatial intervention |

High/low is defined relative to the category-specific median across the 12 subdistricts. It is an exploratory district-relative diagnostic, **not a statutory planning standard**.

### 4. Parks
Park area per resident is retained as supply evidence. Joint park accessibility is deliberately marked pending because parks are areal destinations with potentially multiple entrances; treating one representative point as the access location would introduce avoidable error.

## Key findings

Across the four categories with joint supply–accessibility diagnosis, 16 subdistrict × service cells are classified as combined gaps.

The strongest multi-service concentrations occur in:
- **五角场街道:** combined gaps in 4 service categories
- **长海路街道:** 4
- **大桥街道:** 3
- **殷行街道:** 2

These counts are descriptive overlap evidence rather than an overall ranking of subdistrict quality.

Healthcare and culture require particular interpretive care: the authoritative core inventory contains one principal centre per subdistrict, so differences in facilities per 10,000 residents are driven largely by population denominators rather than centre counts.

## Final outputs

### Maps
1. `outputs/maps/01_supply_pattern.png` — supply pattern
2. `outputs/maps/02_healthcare_accessibility.png` — 15-minute healthcare network accessibility
3. `outputs/maps/03_combined_gap_burden.png` — multi-service combined-gap burden
4. `outputs/maps/04_intervention_diagnostic.png` — dominant intervention diagnostic

### Charts
- `outputs/charts/service_gap_heatmap_final.png` — required 12 × 5 Neighborhood × Service Gap diagnostic matrix
- `outputs/charts/accessibility_profile_final.png` — service-category accessibility profiles

### Core audit tables
- `outputs/tables/service_gap_diagnosis_v1.5.csv`
- `outputs/tables/network_accessibility_by_subdistrict_v1.4.csv`
- `outputs/tables/facility_geometry_qa_v1.3.3.csv`
- `outputs/tables/combined_gap_burden_v1.5.csv`

## Spatial database
`p06_yangpu.gpkg` contains the project’s principal source, QA and analytical layers, including:
- `boundary_subdistrict`
- `population_subdistrict`
- facility layers
- `network_pedestrian_routing_core`
- `facility_accessibility_ready`
- `facility_network_snapped`
- `analysis_supply`
- `analysis_accessibility`
- `analysis_gap`
- `analysis_priority`

## Data and provenance principles
- Prefer authoritative/open sources.
- Preserve source date and provenance.
- Keep unknown capacity as null.
- Do not redistribute the 2024 district population total synthetically to subdistricts.
- Use the authoritative 2020 Census as the transparent subdistrict demand baseline.
- Separate authoritative administrative semantics from operational OSM geometry.
- Treat geocoded coordinates as derived spatial data rather than survey-grade positions.
- Keep unresolved client-type data requirements explicit.

## Reproducibility and QA
The project separates data preparation, supply analysis, accessibility, gap diagnosis and visualization into modular scripts and auditable outputs. Major QA checks include:
- 12-subdistrict boundary topology and district-union checks
- pedestrian-network connectivity checks
- facility geocoding A/B/C evidence
- district containment and subdistrict consistency
- facility-to-network snap distance
- diagnostic-cell completeness
- GeoPackage round-trip verification

See `docs/` for the detailed methodology, limitations, engineering backlog, visual specification and version-specific QA notes.

## Important limitations
1. Subdistrict polygons are operational OSM geometry rather than an official cadastral/administrative polygon dataset.
2. The 2020 Census is the most defensible complete subdistrict population baseline currently available; the 2024 district total is contextual only.
3. Facility geocoding is derived from authoritative addresses and independently QA-checked, but is not survey-grade positioning.
4. Planar network noding can over-connect some grade-separated crossings if bridge/tunnel semantics are incomplete.
5. Accessibility is network-length coverage rather than population coverage.
6. Park accessibility requires entrance-based modelling and is therefore not forced into the current joint diagnostic.
7. Median-based high/low classes describe relative conditions within Yangpu; they do not establish absolute service adequacy.

## Technology
Python · GeoPandas · pandas · NetworkX · Shapely · GeoPackage · QGIS-compatible outputs · Git/GitHub

## Version
**v2.0 — Final analysis and portfolio delivery**

Earlier version-specific QA tables and documentation are retained to preserve the audit trail.
