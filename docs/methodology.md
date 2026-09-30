# Methodology — v0.1

Four analytical layers:
1. Supply — facility count and, where available, service capacity relative to population.
2. Accessibility — network-based access using facility-specific planning/service thresholds.
3. Demand–supply matching — distinguish supply shortage from spatial coverage shortage.
4. Gap & intervention — classify areas by problem type and translate diagnosis into planning actions.

No arbitrary composite ranking is used in the core workflow.


## v1.0 implementation decision
Supply and accessibility are now operationally separated. Authoritative street-level inventory fields may be used for supply indicators even when exact point geometry is unresolved. Network accessibility requires A-grade facility geometry and will not be estimated from street centroids or incomplete candidate sets.
