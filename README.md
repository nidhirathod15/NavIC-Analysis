# NavIC (IRNSS) Geodetic Accuracy & Integrity Analysis
**A Computational Study of India's Regional Navigation Satellite Constellation**

### Objective
This project performs a high-fidelity orbital analysis of the **NavIC (IRNSS)** constellation to validate its reliability for precision positioning. By simulating satellite states over a 24-hour window, the tool quantifies the **Geometric Dilution of Precision (GDOP)**—a critical metric used by agencies like ISRO/NRSC to determine navigation accuracy.

### Performance Summary (24-Hour Study of Mumbai region)
| Metric | Value | Industry Benchmark |
| :--- | :--- | :--- |
| **Average GDOP** | **3.31** | < 6.0 (Excellent) |
| **Peak Precision (Min GDOP)** | **2.46** | Survey-Grade Quality |
| **Satellite Availability** | **8–9** | 100% Redundancy (Min. 4 Req.) |
| **Constellation Uptime** | **100%** | Zero "Outage" Windows |

### Key Insights
**Atmospheric Resilience:** The NavIC hybrid orbit (GEO/IGSO) ensures satellites stay at high elevation angles. This project's **GDOP of 3.31** proves that the geometry is optimized to reduce "Urban Canyon" signal loss in dense Indian cities.
**Deterministic Reliability:** Unlike global systems that vary significantly by latitude, this study confirms that NavIC provides a "fixed" safety net over the Indian subcontinent with double the required satellite count at all times.

### Implementation
1. **Orbital Propagation:** Uses the **SGP4 model** via the `Skyfield` library to ingest real-time TLE (Two-Line Element) data.
2. **Matrix Algebra:** Implemented a **Least-Squares Geometry Matrix** ($G$) and derived the **Covariance Matrix** ($Q = (G^T G)^{-1}$) to extract the Dilution of Precision (DOP).
3. **Geospatial Mapping:** Visualizes real-time "signal footprints" and observer visibility masks using `Folium`.

### Repository Structure
 `main.py`: Core engine for GDOP calculation and real-time tracking.
 `coverage_chart.py`: Script to simulate and visualize 24-hour satellite availability.
 `coverage_chart.png`: Generated proof of 100% system uptime.
 `requirements.txt`: Environment dependencies.
