# Network Accessibility — v1.4

## Analytical scope
Accessibility is measured on the validated pedestrian routing core. Euclidean buffers are not used.

Because the project currently has authoritative population only at subdistrict level, v1.4 does **not** claim fine-scale
population coverage. The reported measure is **pedestrian-network coverage**: the proportion of routing-network length
inside each subdistrict that lies within an estimated 5, 10 or 15 minute walking-network distance of the nearest facility
in a service category.

## Facility-to-network connection
Facilities are projected to their nearest routing edge rather than nearest pre-existing graph node. The projected point is
inserted as a temporary graph source. This avoids the endpoint bias that occurs when a facility lies beside the middle of
a long street segment.

Snap-distance QA:
| facility_type   |   good |   poor |   review |   total |   within_60m_pct |
|:----------------|-------:|-------:|---------:|--------:|-----------------:|
| culture         |      8 |      1 |        1 |      10 |             90   |
| elderly_care    |     45 |      9 |        7 |      61 |             85.2 |
| healthcare      |     10 |      0 |        2 |      12 |            100   |
| park            |     11 |      1 |        5 |      17 |             94.1 |
| sports          |     11 |      4 |        3 |      18 |             77.8 |

Facilities farther than 60 m from the routing core are retained in the facility inventory but excluded from this version's
network service-area calculation pending manual review. 30 m is treated as good; 30–60 m as review-but-usable; >60 m as poor.

## Walking assumptions
A transparent baseline speed of 1.2 m/s is used. Thus 5, 10 and 15 minutes correspond to 360, 720 and 1080 m of network travel.
These are analytical thresholds, not claims that every service category has the same statutory planning radius.

## Interpretation
Network-length coverage describes the spatial reach of the modeled pedestrian network. It is **not** equivalent to resident
population coverage, service capacity, or realized utilization. It should be combined with the supply indicators in the next
gap-diagnosis stage rather than interpreted alone.

## Category ranges across the 12 subdistricts
| facility_type   |   min_5 |   max_5 |   min_10 |   max_10 |   min_15 |   max_15 |
|:----------------|--------:|--------:|---------:|---------:|---------:|---------:|
| healthcare      |     0.7 |    15.5 |      4.5 |     57.1 |     15.4 |     95.4 |
| elderly_care    |     3.2 |    40.5 |     17.5 |     90.5 |     41.1 |    100   |
| culture         |     0   |    18.8 |      0   |     45.6 |      0.1 |     86.8 |
| sports          |     0   |    19.7 |      0   |     69.7 |      0   |     97.3 |
