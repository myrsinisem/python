from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import no_of_stations

stations = build_station_list()

stationsByRiver = stations_by_river(stations)

station_number=rivers_by_station_number(stations, 9)
print(station_number)