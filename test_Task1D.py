from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

#build the list again
stations = build_station_list()
rivers = rivers_with_station(stations)
rivers_list=list(rivers)

rivers_list.sort()

stationsByRiver = stations_by_river(stations) 

print(stationsByRiver['River Cam'])

assert 'Cam' in stationsByRiver['River Cam'] 







