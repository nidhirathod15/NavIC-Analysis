import matplotlib.pyplot as plt
from skyfield.api import load, wgs84
from datetime import timedelta

# Setup
ts = load.timescale()
tle_url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=irnss&FORMAT=tle'
satellites = load.tle_file(tle_url)
mumbai = wgs84.latlon(19.0760, 72.8777)

# Data Collection: Check every hour for the next 24 hours
hours = []
counts = []
start_time = ts.now()

print("Calculating 24-hour coverage data...")

for i in range(24):
    check_time = ts.from_datetime(start_time.utc_datetime() + timedelta(hours=i))
    visible_now = 0
    
    for sat in satellites:
        difference = sat - mumbai
        alt, az, dist = difference.at(check_time).altaz()
        if alt.degrees > 0:
            visible_now += 1
            
    # Convert to IST for the chart labels
    ist_hour = (check_time.utc_datetime() + timedelta(hours=5, minutes=30)).strftime('%H:00')
    hours.append(ist_hour)
    counts.append(visible_now)

# 3. Create the Chart
plt.figure(figsize=(12, 6))
bars = plt.bar(hours, counts, color='skyblue', edgecolor='navy')

# Add a "Red Line" at 4 satellites (the minimum needed for GPS)
plt.axhline(y=4, color='red', linestyle='--', label='Min. for Navigation (4)')

plt.title('NavIC Satellite Availability over Mumbai (Next 24 Hours)', fontsize=14)
plt.xlabel('Time (IST)', fontsize=12)
plt.ylabel('Number of Satellites in View', fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, max(counts) + 2)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()

# Add numbers on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, yval, ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig("coverage_chart.png")
print("Chart saved as coverage_chart.png")
plt.show()