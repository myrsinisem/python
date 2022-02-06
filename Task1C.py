from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations = build_station_list()
stations_radius10 = stations_within_radius(stations, (52.2053, 0.1218),10)
stations_radius10.sort()

print(stations_radius10)

