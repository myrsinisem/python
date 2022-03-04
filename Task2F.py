from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list , update_water_levels
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_station_data
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit

stations = build_station_list()
N=10

update_water_levels(stations)
stations_high_threat = stations_highest_rel_level(stations, N)
j=0 
graph = 0
while (graph < 5):
    station=stations_high_threat[j]
    print(station[0].name)
    dt = 2
    dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=dt))
    j+=1
    if(len(levels)<20):
        continue
    plot_water_level_with_fit(station[0], dates, levels, 4)
    graph+=1