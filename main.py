import numpy as np
from skyfield.api import load, wgs84
from datetime import timedelta

# --- GDOP MATH ENGINE ---
def calculate_gdop(sat_positions, observer_pos):
    if len(sat_positions) < 4: return float('inf')
    rows = []
    for sat_xyz in sat_positions:
        diff = np.array(sat_xyz) - np.array(observer_pos)
        distance = np.linalg.norm(diff)
        rows.append(list(-(diff / distance)) + [1])
    G = np.array(rows)
    try:
        Q = np.linalg.inv(np.dot(G.T, G))
        return np.sqrt(np.trace(Q))
    except: return float('inf')

# --- SETUP ---
ts = load.timescale()
tle_url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=irnss&FORMAT=tle'
satellites = load.tle_file(tle_url)
mumbai = wgs84.latlon(19.0760, 72.8777)
start_time = ts.now()

gdop_list = []

print("Starting 24-Hour NavIC Integrity Analysis...")

# Simulate 48 points (every 30 mins for 24 hours)
for i in range(48):
    current_check = ts.from_datetime(start_time.utc_datetime() + timedelta(minutes=i*30))
    mumbai_xyz = mumbai.at(current_check).position.km
    visible_sats_xyz = []

    for sat in satellites:
        diff = sat - mumbai
        alt, az, dist = diff.at(current_check).altaz()
        if alt.degrees > 0:
            visible_sats_xyz.append(sat.at(current_check).position.km)
    
    val = calculate_gdop(visible_sats_xyz, mumbai_xyz)
    if val != float('inf'):
        gdop_list.append(val)

# --- FINAL RESULTS ---
avg_gdop = np.mean(gdop_list)
max_gdop = np.max(gdop_list)
min_gdop = np.min(gdop_list)

print("-" * 30)
print(f"Result for Mumbai City over 24 Hours:")
print(f"Average GDOP: {avg_gdop:.2f}")
print(f"Best Case (Min): {min_gdop:.2f}")
print(f"Worst Case (Max): {max_gdop:.2f}")
print("-" * 30)