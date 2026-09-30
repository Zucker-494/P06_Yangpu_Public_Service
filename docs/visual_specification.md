# P06 Visual Specification — Acceptance Requirements

Status: requirements frozen; exact symbology to be selected after spatial layers and indicators are available.

## Cartographic requirements
1. No default GIS styling as final output.
2. Strong visual hierarchy: analytical result first, context second.
3. Continuous measures use perceptually ordered, high-contrast continuous ramps where appropriate.
4. Point facilities use deliberate size, stroke, transparency and/or shape; overlapping categories must remain legible.
5. Basemap/context layers are subdued and must not compete with the analytical layer.
6. Legends, labels and symbols remain readable at GitHub README scale and approximately paper single-column scale.
7. Different maps answer different analytical questions; avoid repeating the same choropleth with different variables.
8. Export resolution and dimensions will be standardised across the final figure family.

## Required analytical roles
- Facility/supply pattern
- Network accessibility
- Demand–supply mismatch
- Gap/diagnostic type
- Intervention priority

## Required non-map analytical figure
Neighborhood × Service Gap Heatmap (12 subdistricts × service categories).

Heatmap cells must derive from transparent reproducible diagnostic rules, not subjective composite scoring.
