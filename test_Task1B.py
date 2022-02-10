from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
#Test for 1B
#build the list of the stations

stations = build_station_list()
stations_sorted = stations_by_distance(stations, (52.2053, 0.1218))
assert len(stations_sorted) >0

#Test for 1C
#build list of stations withing radius 


