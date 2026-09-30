# Facility Geocoding QA — v1.3.2

## Source and role
Facility coordinates were obtained from Baidu's server-side geocoding service using the authoritative address fields already stored in the P06 source inventories. API success is treated only as a coordinate candidate, not as proof of analytical readiness.

The returned BD-09 coordinates are converted to GCJ-02 and then WGS84 before spatial QA against the project's Yangpu subdistrict geometry.

## QA dimensions
1. API success and coordinate presence.
2. Point contained within Yangpu District.
3. Spatially joined subdistrict compared with the authoritative source subdistrict where available.
4. Baidu `precise`, `confidence`, and `level`.
5. Duplicate-coordinate clustering as a warning for coarse or repeated geocodes.

## Confidence rule
**A** requires: successful geocoding; Yangpu containment; no contradiction with a known official subdistrict; `precise=1`; confidence >= 70; acceptable address/POI-level result; and no >2-facility identical-coordinate cluster.

**B** is a plausible Yangpu result that fails one of the stricter precision criteria but is not obviously coarse/contradictory.

**C** includes failed/missing addresses, locations outside Yangpu, authoritative-subdistrict contradictions, coarse results, low-confidence results, or suspicious coordinate clustering.

Only A is used for category-wide accessibility.

## Category readiness
| facility_type   |   official_total |   api_success |   within_yangpu |   A |   B |   C |   A_coverage_pct | gate_80_status   |
|:----------------|-----------------:|--------------:|----------------:|----:|----:|----:|-----------------:|:-----------------|
| culture         |               12 |             8 |               8 |   7 |   1 |   4 |          58.3333 | not_ready        |
| elderly_care    |               65 |            65 |              65 |  46 |  18 |   1 |          70.7692 | not_ready        |
| healthcare      |               12 |            12 |              12 |  12 |   0 |   0 |         100      | ready            |
| park            |               22 |            22 |              22 |  16 |   0 |   6 |          72.7273 | not_ready        |
| sports          |               20 |            20 |              20 |  16 |   3 |   1 |          80      | ready            |

The 80% A-coverage rule remains an internal project QA gate rather than an external planning standard.
