from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()
rivers = rivers_with_station(stations)
rivers_list=list(rivers)

rivers_list.sort()

print(len(rivers_list))
print(rivers_list[:10])

stationsByRiver = stations_by_river(stations) 

print(sorted(stationsByRiver["River Aire"]))
print(sorted(stationsByRiver["River Cam"]))
print(sorted(stationsByRiver["River Thames"]))