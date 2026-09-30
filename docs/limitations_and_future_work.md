# Limitations and Future Work

This document records known data and analytical limitations as part of the project's data-governance process. A limitation is not treated as a hidden defect: each item is linked to its analytical consequence, the current mitigation, and a concrete upgrade path.

| Limitation | Analytical consequence | Current treatment | Future work |
|---|---|---|---|
| Operational subdistrict polygons are derived from the 2026-09-28 Geofabrik/OSM snapshot rather than an official government GIS boundary dataset. | Small area differences may occur relative to published administrative statistics. | Official Shanghai Civil Affairs names/codes define administrative semantics; OSM geometry passed validity, topology and district-union QA. Geometry provenance is retained explicitly. | Replace the operational geometry with an official polygon layer if it becomes available, then rerun all spatial analyses. |
| Subdistrict demand uses the 2020 Seventh Population Census, while a 2024 district-level population control total is available. | Population-standardised indicators represent a census-baseline demand condition rather than a strict 2024 current-state estimate. | The 2024 district total is used only as temporal context; it is not proportionally redistributed to streets. | Replace the demand baseline with authoritative updated subdistrict/community population when available. |
| Population is currently available only at subdistrict level. | Intra-subdistrict population concentration cannot yet be represented in accessibility or demand surfaces. | Supply rates are calculated at the same subdistrict aggregation level. No synthetic fine-scale population is created. | Introduce community/residential-committee population, validated population grids, or building-level population estimates. |
| Facility point geometry is incomplete and spatial evidence varies by service category. | Incomplete coordinates would bias network accessibility and service-area estimates. | Candidate geometry is managed with A/B/C confidence. Only A-grade geometry is eligible for accessibility analysis. Unresolved official facilities remain in the inventory without guessed coordinates. | Resolve locations using official coordinates, additional authoritative spatial data, or auditable manual verification. |
| OSM address tags are incomplete for the official facility inventory. | OSM/PBF alone cannot geocode all facilities reliably. | Official inventories remain the entity source of truth; OSM is used only as supporting spatial evidence. | Integrate a more complete authoritative address/POI source where licensing permits. |
| The frozen sports inventory does not contain an authoritative subdistrict field. | Street-level sports supply cannot yet be estimated without potentially biased spatial assignment. | Sports is excluded from current street-level supply diagnostics. | Resolve sports locations and assign subdistricts by validated spatial join. |
| Capacity data are incomplete and not fully temporally harmonised across elderly-care and healthcare facilities. | Facility counts cannot be interpreted as equivalent service capacity. | Known capacity is analysed separately; unknown values remain null and are never imputed without evidence. | Obtain harmonised licensed beds, staffing, floor area, throughput, or other service-capacity measures. |
| Facility datasets have different reference years. | Cross-service comparisons contain temporal mismatch. | Every dataset retains its source/reference date and results are interpreted as a multi-source planning snapshot. | Rebuild the database using a harmonised reference year when updated inventories become available. |
| No observed resident trip or facility-utilisation data are available. | Modelled accessibility represents potential spatial access rather than realised service use. | Findings are framed as spatial provision/accessibility evidence, not observed behaviour. | Integrate visit records, travel surveys, service utilisation, or mobility data where legally and ethically available. |
| Current supply diagnostics use district-relative statistics rather than official service standards. | “Below median” does not mean objectively inadequate, and “above median” does not mean sufficient. | Median splits are used only as transparent exploratory screening. Final service-gap classes remain pending accessibility and, where available, planning standards/capacity evidence. | Introduce service-specific normative thresholds from authoritative planning standards and sensitivity-test diagnostic classifications. |

## Analytical upgrade path

Current public-data implementation:

**authoritative inventories → subdistrict supply → validated network accessibility → demand–supply diagnosis → intervention type**

Future operational implementation:

**official GIS + finer population + complete facility coordinates + harmonised capacity + observed utilisation → fine-scale accessibility → target-group demand → capacity-sensitive gap diagnosis → site/capacity/resource intervention**

The architecture is intentionally designed so that improved datasets can replace weaker inputs without changing the overall analytical logic.


## v1.2 status note
The first visual-evidence audit confirmed that not every available supply indicator should be mapped. Healthcare and culture rates are strongly shaped by the one-centre-per-subdistrict institutional structure, while park area per resident and elderly-care facility density contain more substantive between-subdistrict supply variation. Sports remains excluded from street-level diagnostics until location-based assignment is sufficiently verified.


## v1.3 network status
A pedestrian-network candidate has been extracted from the 2026-09-29 OSM PBF snapshot with a 1 km routing buffer. Network QA is now implemented. However, facility geometry—not network availability—is the principal constraint on category-wide accessibility analysis. An explicit 80% A-grade geometry gate is used internally to prevent incomplete facility sets from producing misleading service-area results.


## v1.3.1 topology note
The v1.3 endpoint-only graph substantially under-connected the pedestrian network because source line intersections were not necessarily represented as line endpoints. v1.3.1 applies planar noding to recover geometric junctions. This fixes the dominant under-connection problem, but introduces a smaller opposite risk: grade-separated bridge/tunnel crossings may be connected geometrically if vertical/topological OSM tags are not preserved through noding. Final routing should therefore retain or reconstruct OSM grade-separation semantics where material.


## v1.3.2 geocoding provenance
Facility point geometry is derived from authoritative inventory addresses using Baidu geocoding rather than from an authoritative coordinate register. Coordinates are therefore treated as derived spatial data. The original address remains the source-of-record attribute, and geocoder precision/confidence plus independent district/subdistrict spatial checks are retained for QA. BD-09 coordinates are transformed to WGS84 for integration with the project database; transformation itself introduces small positional uncertainty that is immaterial for subdistrict assignment but should not be interpreted as survey-grade positioning.
