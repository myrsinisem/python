from ast import Continue
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_station_data
     
stations = build_station_list()

update_water_levels(stations)

def test_stations_level_over_threshold1():
    tol = 0.2
    stations_thresh = stations_level_over_threshold(stations, tol)
    list = []
    for station in stations_thresh:
        list.append(station[0].name) 
    assert len(list) > 10

#tolerance is low 0.2 so it should always print more than 10 --> test is universal


def test_stations_level_over_threshhold2():
    tol = 0.8
    update_water_levels(stations)
    stations_above_level = stations_level_over_threshold(stations, tol)

    for stations in stations_above_level:
        assert stations[1] > 0.8
        assert stations[2] > 0.8



stations_high_threat = stations_highest_rel_level(stations, 10)
     
list2 = []
for station in stations_high_threat:
    list2.append(station[0].name)

assert len(list2) == 10
