from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

stations = build_station_list()
rivers = rivers_with_station(stations)

station_number=rivers_by_station_number(rivers, 9)
print(station_number)