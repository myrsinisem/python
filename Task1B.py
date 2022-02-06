from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()
stations_sorted = stations_by_distance(stations, (52.2053, 0.1218))

print(stations_sorted[:10])
print(stations_sorted[-10:])
