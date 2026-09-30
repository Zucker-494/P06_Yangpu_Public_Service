# Pedestrian Topology Repair — v1.3.1

## Problem identified in v1.3
The initial QA graph used only the endpoints of source OSM line features. Many geometrically intersecting streets were therefore not represented as graph junctions, producing severe artificial fragmentation.

## Repair
The pedestrian linework was planar-noded: line geometry was split at geometric intersections and a new endpoint graph was constructed from the resulting segments.

## Result
| metric                         |        value | unit       | status   |
|:-------------------------------|-------------:|:-----------|:---------|
| noded_segments                 | 16424        | count      | INFO     |
| graph_nodes                    | 11706        | count      | INFO     |
| graph_edges                    | 16291        | count      | INFO     |
| connected_components           |    80        | count      | INFO     |
| largest_component_node_share   |     0.972493 | proportion | PASS     |
| largest_component_length_share |     0.988198 | proportion | PASS     |
| largest_component_length_km    |  1191.82     | km         | INFO     |
| total_graph_length_km          |  1206.06     | km         | INFO     |

The repair substantially improves connectivity. The largest component is retained as `network_pedestrian_routing_core`; the complete noded linework remains available as `network_pedestrian_noded`.

## Important residual limitation
Planar noding can falsely connect grade-separated crossings (bridges/tunnels) if layer/bridge/tunnel information is not carried through the geometric union. Therefore v1.3.1 should be treated as a routing-core candidate rather than unquestioned ground truth.

Before final accessibility modelling:
1. inspect whether the largest component dominates both nodes and network length;
2. review obvious bridge/tunnel crossings and isolated components;
3. where necessary, reconstruct topology using OSM node identity and grade-separation tags rather than geometry alone.

This limitation is preferable to the opposite error in v1.3, where true at-grade intersections were systematically missed.
