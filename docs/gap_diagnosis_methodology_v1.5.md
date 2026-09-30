# Demand–Supply Gap Diagnosis — v1.5

## Purpose
v1.5 combines the supply evidence with v1.4 pedestrian-network accessibility to identify **types of service gap** rather
than collapse heterogeneous evidence into an arbitrary weighted score.

## Diagnostic rule
For healthcare, elderly care, culture and sports, each subdistrict is classified relative to the category-specific median
supply and median 15-minute network coverage across the 12 Yangpu subdistricts:

| Supply | Accessibility | Diagnostic type | Planning interpretation |
|---|---|---|---|
| High | High | broadly adequate | maintain and monitor |
| High | Low | spatial configuration gap | redistribute access points or add spatially targeted provision |
| Low | High | supply/capacity pressure | expand provision/capacity before assuming a siting problem |
| Low | Low | combined gap | combined supply and spatial intervention |

The median split is a **relative exploratory diagnostic**, not a statutory service standard and not proof of absolute adequacy.
Consequently, “broadly adequate” means comparatively stronger within this dataset, not that every resident is adequately served.

## Supply indicators
- Healthcare: community health service centres per 10,000 residents.
- Elderly care: authoritative elderly-care facility count per 10,000 residents.
- Culture: community cultural activity centres per 10,000 residents.
- Sports: A-grade spatially validated sports facilities per 10,000 residents.
- Parks: park area per capita is retained as supply evidence, but joint accessibility diagnosis is deferred.

Healthcare and culture each have one principal centre per subdistrict in the authoritative inventory. Their per-capita supply
differences therefore mainly reflect the population denominator and must not be interpreted as differences in centre count.

## Accessibility indicator
The joint diagnosis uses v1.4 **15-minute pedestrian-network coverage**, defined as the share of modeled pedestrian-network
length within each subdistrict that lies within 15 minutes of the nearest usable facility. It is not population coverage.

## Parks
Parks are deliberately marked `accessibility pending`. A park is an areal destination with potentially multiple entrances;
using a single representative point would create avoidable methodological error. Park supply remains visible in the heatmap,
but parks are excluded from combined-gap priority identification until entrance-based accessibility is available.

## Priority interpretation
`combined_gap` identifies areas where both relative supply and modeled spatial reach are below their category medians.
No weighted ranking is imposed among these areas. The cross-category count is descriptive: it shows how many service
categories simultaneously exhibit a combined gap in each subdistrict.

## Diagnostic counts
| facility_type   |   broadly_adequate |   combined_gap |   spatial_configuration_gap |   supply_capacity_pressure |
|:----------------|-------------------:|---------------:|----------------------------:|---------------------------:|
| culture         |                  4 |              4 |                           2 |                          2 |
| elderly_care    |                  4 |              4 |                           2 |                          2 |
| healthcare      |                  4 |              4 |                           2 |                          2 |
| sports          |                  4 |              4 |                           2 |                          2 |

## Reproducibility
The complete cell-level diagnostic table is `outputs/tables/service_gap_diagnosis_v1.5.csv`.
The 12 × 5 matrix is `outputs/tables/neighborhood_service_gap_heatmap_matrix_v1.5.csv`.
