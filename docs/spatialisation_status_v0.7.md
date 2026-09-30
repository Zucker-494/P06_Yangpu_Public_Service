# Spatialisation Status — v0.7

## Completed
- Authoritative 12-subdistrict semantic reference is frozen.
- Time-aware official area QA reference table created.
- Reproducible OSM/Geofabrik boundary acquisition entry point created.
- Boundary geometry QA script created.
- Controlled GeoPackage build entry point created.
- Visual acceptance specification remains binding.

## Not falsely claimed as complete
- The Shanghai OSM GeoPackage could not be downloaded automatically in the current execution environment.
- No operational subdistrict polygon is therefore included yet.
- Facility addresses have not been silently geocoded through an undocumented service.
- `p06_yangpu.gpkg` will only be built after approved spatial geometry exists.

## Next execution gate
Acquire candidate polygon geometry → reconcile 12 names → geometry/topology/area QA → approve `boundary_subdistrict` → geocode/validate facility locations → build GeoPackage.

## v0.8 update
The user supplied the Geofabrik Shanghai free GeoPackage snapshot dated 2026-09-28.
The 12 current Yangpu subdistrict polygons were successfully extracted from the administrative-area layer and passed geometry/topology/district-union QA.
The approved operational boundary is now stored in `data/processed/boundary_subdistrict.gpkg` and `p06_yangpu.gpkg`.
The project GeoPackage also contains a population-subdistrict polygon layer joined to the frozen 2020 Census demand baseline.
