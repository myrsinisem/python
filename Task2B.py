from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list , update_water_levels
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_station_data


stations = build_station_list()
tol = 0.8

update_water_levels(stations)
stations_thresh = stations_level_over_threshold(stations, tol)
     
for station in stations_thresh:
    print(station[0].name, station[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
