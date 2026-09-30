# Pedestrian Network and Accessibility Readiness — v1.3

## Network source
The pedestrian-network candidate is extracted directly from the user-supplied `shanghai-260929.osm.pbf` snapshot. A 1 km buffer around Yangpu is retained to reduce artificial routing truncation at the district boundary.

## Pedestrian filtering
Ways with an OSM `highway` tag are retained unless they are explicitly unsuitable for pedestrian routing, including:
- `foot=no` or private pedestrian access;
- motorway/motorway_link;
- `motorroad=yes`;
- construction/proposed/raceway without explicit pedestrian permission.

Original road class and access-related attributes are retained for audit.

## Network QA
| metric                       |       value | unit       | status   |
|:-----------------------------|------------:|:-----------|:---------|
| walkable_line_features       | 7308        | count      | INFO     |
| network_total_length_km      | 1221.46     | km         | INFO     |
| graph_nodes                  | 9844        | count      | INFO     |
| graph_edges                  | 7185        | count      | INFO     |
| connected_components         | 3214        | count      | REVIEW   |
| largest_component_node_share |    0.180821 | proportion | REVIEW   |
| routing_buffer_m             | 1000        | m          | INFO     |

The endpoint graph is used as a conservative QA diagnostic. Multiple components may partly reflect unsplit OSM line intersections, grade separation, or the endpoint-only construction used at this stage. It is therefore not yet treated as the final routing graph.

## Facility geometry gate
| facility_type   |   A |   B |   C |   total |   A_coverage_pct |   required_A_coverage_pct | accessibility_status   |
|:----------------|----:|----:|----:|--------:|-----------------:|--------------------------:|:-----------------------|
| culture         |   0 |   0 |  12 |      12 |          0       |                        80 | not_ready              |
| elderly_care    |   0 |   5 |  60 |      65 |          0       |                        80 | not_ready              |
| healthcare      |   1 |   4 |   7 |      12 |          8.33333 |                        80 | not_ready              |
| park            |   1 |  11 |  10 |      22 |          4.54545 |                        80 | not_ready              |
| sports          |   0 |   1 |  19 |      20 |          0       |                        80 | not_ready              |

For category-wide accessibility modelling, v1.3 uses a conservative readiness gate of **80% A-grade facility geometry**. This is a project QA rule, not an external planning standard.

No service category currently passes this gate. Therefore `analysis_accessibility` is intentionally not produced in v1.3.

## Consequence
The network itself is now available and auditable, but facility-location completeness remains the binding constraint. The next stage should either:
1. improve facility geometry through authoritative/manual verification; or
2. transparently narrow the accessibility question to a service category with sufficiently complete validated locations.

Street centroids and unresolved candidate points will not be substituted for missing facility locations.
