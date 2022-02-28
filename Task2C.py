from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list , update_water_levels
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_station_data


stations = build_station_list()
N=10

update_water_levels(stations)
stations_high_threat = stations_highest_rel_level(stations, N)
     
for station in stations_high_threat:
    print(station[0].name, station[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
