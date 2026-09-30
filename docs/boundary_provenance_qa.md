# Subdistrict Boundary Provenance and QA — v0.6

## Authoritative semantic reference
The current Yangpu administrative framework contains 12 subdistricts. Names and administrative codes are taken from Shanghai Civil Affairs sources.

Yangpu planning documents explicitly use street administrative boundaries to define the 12 planning units.

## Geometry status
A directly downloadable official polygon dataset for all 12 Yangpu subdistricts has not yet been verified.

Therefore:
- administrative names/codes must remain authoritative;
- any open-source polygon geometry used operationally must be labelled by its actual geometry source;
- no third-party/open polygon may be described as an official boundary;
- geometry must pass QA before analytical use.

## Required geometry QA
1. Exactly 12 unique subdistrict polygons after cleaning.
2. Names/codes reconcile to the authoritative 12-unit reference table.
3. Union is spatially consistent with the Yangpu district extent.
4. No unexplained overlaps or internal gaps.
5. Adjacency is checked against official street descriptions/planning maps where practical.
6. Area values are compared with official subdistrict area descriptions when available.
7. CRS and geometry source/version are recorded.

## Analysis rule
No facility-to-subdistrict spatial join or accessibility aggregation is final until the boundary layer passes this QA.
