from ast import Continue
import floodsystem.flood 
from floodsystem.stationdata import build_station_list


def test_stations_level_over_threshhold():
    stations = build_station_list
    test_list=[]
    for station in stations:
        if station.relative_water_level() == None:
            continue
        elif station.relative_water_level() > 0.8:
            list.append((station))
        assert len(list) !=0

def test_stations_highest_rel_level():
    stations = build_station_list
    list = []
    for station in stations:
        if station.relative_water_level() == None:
            continue
        else:
            list.append(station)
    assert len(list) > 0

