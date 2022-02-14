from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


stations=build_station_list()
inconsistent_stations=inconsistent_typical_range_stations(stations)
sorted_stations=sorted(inconsistent_stations)

assert sorted_stations[0]=="Airmyn"
assert "Fleetwood" in inconsistent_stations