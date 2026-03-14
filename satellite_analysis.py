"""
Satellite Ground Track and India Pass Analysis
This script demonstrates how orbital data from TLE (Two-Line Element) datasets
can be used to compute the ground track of an Earth-orbiting satellite.

The program performs the following tasks:
1. Loads satellite orbital parameters from TLE data
2. Propagates the satellite orbit over a full day
3. Computes latitude/longitude positions of the satellite subpoint on Earth
4. Detects when the satellite passes over the geographic region of India
5. Estimates revisit interval over the region
6. Visualizes the satellite ground track and India passes
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from skyfield.api import load, EarthSatellite

# CONFIGURATION
# This section defines the satellite we want to analyse and the simulation settings for the orbit propagation.
TLE_NAME = "ISS"

# TLE (Two-Line Element) data describing the satellite orbit. These values are used by the Skyfield library to propagate the satellite position at different timestamps.
TLE_LINE1 = "1 25544U 98067A   24123.54791667  .00016717  00000+0  10270-3 0  9004"
TLE_LINE2 = "2 25544  51.6434 159.2012 0006781  39.4287  58.4145 15.50000000 00000"

# Start date of the orbit simulation
START_DATE = (2024, 5, 1)

# Number of simulation steps. 1440 steps = 1 position per minute for 24 hours
TIME_STEPS = 1440

# Geographic bounding box for India
# These values represent approximate spatial limits used to detect when the satellite is above India.
INDIA_LAT = (8.07, 37.10)
INDIA_LON = (68.12, 97.42)

# Output files
OUTPUT_DATA = "results/satellite_positions.csv"

# CREATE RESULTS DIRECTORY
os.makedirs("results", exist_ok=True)

# LOAD SATELLITE USING SKYFIELD
# Skyfield loads the satellite using TLE data and prepares the time scale used for orbit propagation.
ts = load.timescale()
sat = EarthSatellite(TLE_LINE1, TLE_LINE2, TLE_NAME, ts)

# Create timestamps for each simulation step
t = ts.utc(START_DATE[0], START_DATE[1], START_DATE[2], range(TIME_STEPS))

# COMPUTE SATELLITE POSITIONS
# The satellite position is converted to the "subpoint" which is the latitude/longitude point on Earth directly beneath the satellite.
subpoint = sat.at(t).subpoint()

latitudes = subpoint.latitude.degrees
longitudes = subpoint.longitude.degrees

# Store computed data in a DataFrame for easier analysis
df = pd.DataFrame({
    "latitude": latitudes,
    "longitude": longitudes,
    "time_index": range(len(latitudes))
})

print("Satellite positions calculated:", len(df))

# SAVE DATA FOR FUTURE ANALYSIS
# This CSV file stores all calculated satellite positions and can be reused for GIS or orbit analysis later.

df.to_csv(OUTPUT_DATA, index=False)

# DETECT SATELLITE PASSES OVER INDIA
# We filter all coordinates that fall within India's geographic bounding box.

india_passes = df[
    (df["latitude"] >= INDIA_LAT[0]) &
    (df["latitude"] <= INDIA_LAT[1]) &
    (df["longitude"] >= INDIA_LON[0]) &
    (df["longitude"] <= INDIA_LON[1])
]

print("Satellite passes over India:", len(india_passes))

# VISUALISE SATELLITE PASSES OVER INDIA
# Only the positions above India are plotted.
# This gives a clear visual representation of satellite
# coverage over the region.

fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection=ccrs.PlateCarree())

ax.coastlines()
ax.gridlines(draw_labels=True)

plt.scatter(
    india_passes["longitude"],
    india_passes["latitude"],
    s=20,
    color="red"
)

plt.title("Satellite Passes Over India")
plt.show()

# REVISIT INTERVAL ESTIMATION
# Revisit time represents how frequently the satellite returns to the same geographic region.
if len(india_passes) > 1:
    revisit_time = india_passes.time_index.diff().mean()
    print("Average revisit interval (minutes):", revisit_time)
else:
    print("Not enough passes to compute revisit time.")

print("Satellite data saved:", OUTPUT_DATA)