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
for i in range (0,4):
    (station,a)=stations_high_threat[i]
    print(station)
    dt = 2
    dates, levels = fetch_measure_levels(station.get_measureID(), dt=datetime.timedelta(days = 2))
    print (dates)
    plot_water_level_with_fit(station, dates, levels, 4)
    j+=1
