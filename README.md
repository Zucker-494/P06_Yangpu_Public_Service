# P06 — Yangpu Public Service Assessment and Spatial Decision Support

## Status
P06-05: Data Acquisition & Preparation — v0.3 (parks + authoritative elderly-care inventory)

## Project type
Independent portfolio project simulating a Chinese GIS/planning horizontal-project workflow.

## Study area
Yangpu District, Shanghai. Primary reporting units: 12 subdistricts.

## Core question
Where are public-service provision, accessibility, and demand–supply mismatches located, and what type of intervention should be prioritised?

## Current implementation
Python / GeoPandas + GeoPackage + QGIS. No new software is required during the thesis-submission period.

## Workflow
Raw data → standardisation → spatial integration → supply analysis → accessibility analysis → gap diagnosis → decision-support outputs.

## Important
This is a simulated consultancy workflow, not a commissioned project. Official/authoritative data are preferred. Missing client-type datasets remain explicit data requirements rather than being silently replaced by weak proxies.


## Data acquisition status
The first authoritative facility layer has been acquired: the official Yangpu district park register (22 records). Additional official sources for elderly care, healthcare, culture and sports have been identified and are being consolidated before spatial analysis begins.

- Elderly-care layer: 65 official 2024 institution/service-home records added; planning capacity is maintained as a separate, typed source.
