# Facility Geometry QA Revision — v1.3.3

## Method correction
v1.3.2 used an unnecessarily narrow whitelist of Baidu `level` values. Baidu documents `precise=1` as accurate geocoding and
allows many legitimate `level` categories. v1.3.3 therefore retains `level` as diagnostic metadata rather than a hard whitelist.

## Strict Baidu A gate
A requires successful geocoding, `precise=1`, confidence >=70, Yangpu containment, no contradiction with a known authoritative
subdistrict, and no suspicious >2-record identical-coordinate cluster. Confidence and precise remain provenance/quality metadata;
these coordinates are not treated as survey-grade positions.

## Independent cross-source upgrades
Authoritative source evidence plus independently named OSM entities supports A-grade geometry for:
- 唐家塔口袋公园
- 四平路街道社区文化活动中心
- 新江湾城街道社区文化活动中心

## Official culture-address enrichment
Current Yangpu Government material supports:
- 大桥街道社区文化活动中心 — 平凉路1730号
- 延吉新村街道社区文化活动中心 — 延吉中路77号
- 四平路街道社区文化活动中心 — 抚顺路360号
- 新江湾城街道社区文化活动中心 — 国秀路700号

Address evidence alone is not converted into geometry. 大桥 and 延吉 remain pending independent coordinate verification.

## Category readiness
| facility_type   |   total |   A |   B |   C |   A_coverage_pct | gate_80_status   |
|:----------------|--------:|----:|----:|----:|-----------------:|:-----------------|
| culture         |      12 |  10 |   0 |   2 |             83.3 | ready            |
| elderly_care    |      65 |  61 |   3 |   1 |             93.8 | ready            |
| healthcare      |      12 |  12 |   0 |   0 |            100   | ready            |
| park            |      22 |  17 |   0 |   5 |             77.3 | not_ready        |
| sports          |      20 |  18 |   1 |   1 |             90   | ready            |

The 80% threshold is an internal completeness gate, not a statutory adequacy standard.
