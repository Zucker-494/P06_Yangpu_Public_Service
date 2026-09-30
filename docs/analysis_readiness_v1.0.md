# v1.0 Analysis Readiness

## Why supply and accessibility are separated
The official facility inventories already support subdistrict-level supply analysis where a trusted subdistrict field exists.
Network accessibility is different: it requires reliable point geometry. Candidate coordinates are therefore not allowed to contaminate accessibility results.

## Geometry confidence rule
- **A**: strong facility-entity name agreement plus strong address evidence, with subdistrict consistency where an official subdistrict is available.
- **B**: strong entity evidence *or* strong address evidence, but not both; retained for review.
- **C**: weak/ambiguous candidate; not used analytically.
Only A is marked `analysis_ready_accessibility = True`.

## Current candidate evidence
| facility_type   |   A |   B |   C |   total |
|:----------------|----:|----:|----:|--------:|
| culture         |   0 |   0 |  12 |      12 |
| elderly_care    |   0 |   5 |  60 |      65 |
| healthcare      |   1 |   4 |   7 |      12 |
| park            |   1 |  11 |  10 |      22 |
| sports          |   0 |   1 |  19 |      20 |

The stricter v1.0 rule intentionally downgrades address-only matches. A matching street/house number is not sufficient proof that the OSM object represents the same facility.

## Supply analysis
`analysis_supply` is now built for parks, elderly care, healthcare, and culture from authoritative inventories plus the frozen 2020 Census street-level population baseline.

Indicators include:
- facility count;
- facilities per 10,000 residents;
- registered park area and park area per resident;
- known capacity totals where actual/supported capacity fields exist.

Unknown capacity remains null and is never imputed.

## Sports
The 20-record sports inventory is retained, but street-level sports supply is deferred because the frozen source table does not contain an authoritative `subdistrict_name` field and current geocoding coverage is insufficient for unbiased assignment.

## Accessibility
`analysis_accessibility` is deliberately not created in v1.0. Accessibility starts only after point coverage is sufficiently complete and auditable.
