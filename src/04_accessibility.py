"""
Accessibility stage gate.

The pedestrian network is stored in p06_yangpu.gpkg/network_pedestrian.
Do not calculate category-wide network accessibility until the relevant
facility category reaches the documented A-grade geometry completeness gate.

Missing facilities must not be replaced with street centroids.
The final routing graph must also split true at-grade intersections before
shortest-path/service-area computation.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
gate = pd.read_csv(ROOT/"outputs/tables/accessibility_gate_v1.3.csv")
ready = gate.loc[gate["accessibility_status"].eq("ready"), "facility_type"].tolist()
print("Accessibility-ready categories:", ready)
