from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list , update_water_levels

stations = build_station_list()
def stations_level_over_threshold(stations, tol):
    list=[]
    for station in stations:
        if station.relative_water_level() == None:
            continue
        elif station.relative_water_level() > tol:
            list.append((station, station.relative_water_level()))
    return sorted_by_key(list, 1, True)


def stations_highest_rel_level(stations,N):
    list=[]
    for station in stations:
        if station.relative_water_level() == None:
            continue
        else:
            list.append((station, station.relative_water_level()))
    list_sorted = sorted_by_key(list, 1, True)
    return list_sorted[:N]

    