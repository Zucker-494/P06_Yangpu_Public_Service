# Data Dictionary — v0.1

## Core reporting unit
`subdistrict_id`, `subdistrict_name`, `geometry`

## Population
`subdistrict_id`, `subdistrict_name`, `population_total`, `population_elderly`,
`reference_year`, `source`

`population_total` must refer to the latest available authoritative resident-population
measure used for the project. Migrant-population counts must not be substituted for total
resident population.

## Standard facility schema
`facility_id`, `facility_name`, `facility_type`, `subtype`, `address`, `subdistrict_name`,
`source`, `source_date`, `capacity`, `capacity_unit`, `geometry`

Unknown capacity remains null; it is not imputed without a defensible source.
