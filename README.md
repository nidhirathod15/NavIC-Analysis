# NavIC (IRNSS) Geodetic Accuracy & Satellite Pass Analysis
A computational study of India's regional navigation satellite system and satellite ground track behaviour over the Indian subcontinent.

# Project Overview
This repository contains two small satellite analysis experiments built using Python. The goal of the project is to explore how satellite orbital data can be used to analyse:
• Navigation satellite positioning accuracy
• Satellite coverage over India
• Ground track behaviour of Earth-orbiting satellites
The project uses publicly available orbital data and propagates satellite positions to analyse satellite visibility and positioning geometry.

# Part 1 — NavIC (IRNSS) Geodetic Accuracy Analysis
India's regional navigation system **NavIC** (also known as **IRNSS**) provides accurate positioning, navigation, and timing information for users in India and nearby regions, supporting applications such as vehicle navigation, disaster management, mapping, and timing services. This project performs a computational analysis of the constellation to estimate positioning reliability over a 24-hour period. Using satellite orbital data, the system geometry is analysed to estimate **Dilution of Precision (DOP)** — a standard navigation metric used to evaluate how satellite geometry affects positioning accuracy.

# Objective
The objective of this analysis is to simulate NavIC satellite states over a 24-hour window and estimate the quality of positioning over the Mumbai region. This helps evaluate whether the satellite geometry provides sufficient accuracy and redundancy for reliable navigation.

# Performance Summary
24-Hour Simulation — Mumbai Region

| Metric                    | Value          | Industry Benchmark   |
| ------------------------- | -------------- | -------------------- |
| Average GDOP              | 3.31           | < 6.0 (Excellent)    |
| Peak Precision (Min GDOP) | 2.46           | Survey-grade quality |
| Satellite Availability    | 8–9 satellites | Minimum 4 required   |
| Constellation Uptime      | 100%           | No outage windows    |

# Key Insights
# High Elevation Satellite Geometry
NavIC uses a hybrid orbital architecture consisting of geostationary and inclined geosynchronous satellites. Because of this design, satellites remain at relatively high elevation angles over India. This reduces signal blockage in dense urban environments. The calculated GDOP value of **3.31** indicates that the satellite geometry provides strong positioning accuracy over the region.

# Regional Reliability
Unlike global navigation systems whose satellite visibility varies by latitude, NavIC is specifically designed to prioritise the Indian region. The analysis shows that the constellation consistently maintains more than the minimum number of satellites required for positioning. This ensures continuous coverage over the subcontinent.

# Part 2 — Satellite Ground Track and India Pass Detection
The second part of the project analyses how satellite orbits translate into ground coverage over India.
Using orbital parameters from a **Two-Line Element (TLE)** dataset, the program simulates satellite positions over a 24-hour period and calculates the ground track of the satellite.
The program then detects when the satellite passes over India by filtering coordinates within the country's geographic boundaries.

# What the Program Does
The program performs the following steps:
1. Loads satellite orbital parameters from a TLE dataset
2. Propagates the satellite orbit for 24 hours
3. Computes the satellite ground position every minute
4. Stores all coordinates in a dataset
5. Detects when the satellite passes over India
6. Estimates revisit intervals over the region

# Output
Output from the simulation:
Satellite positions calculated: 1440
Satellite passes over India: 27
Average revisit interval: ~53 minutes
This indicates how frequently the satellite appears above the Indian region within the simulation window.

# Implementation
The project uses several standard orbital analysis and scientific computing tools.

# Orbital Propagation
Satellite motion is propagated using the **SGP4 orbital model** implemented through the **Skyfield** Python library. Orbital parameters are read from publicly available **TLE (Two-Line Element)** datasets.

# Navigation Geometry Analysis
For the NavIC positioning analysis, the project constructs a **geometry matrix (G)** from satellite line-of-sight vectors.
The covariance matrix is then calculated using:
Q = (GᵀG)⁻¹
From this matrix, Dilution of Precision (DOP) metrics are derived.

# Geospatial Visualisation
Satellite ground positions are visualised using:
• Matplotlib
• Cartopy
These tools allow satellite passes over India to be displayed on a geographic map.

# Technologies Used
The project is made entirely using Python.
Main libraries:
* numpy
* pandas
* matplotlib
* cartopy
* skyfield
* folium

# Applications
Satellite orbit analysis like this is useful for:
• Satellite mission planning
• Earth observation coverage studies
• Navigation system reliability analysis
• Remote sensing mission scheduling

Understanding satellite visibility and ground tracks is essential for designing reliable space systems.
Nidhi Rathod
B.Tech Data Science
