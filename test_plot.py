from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level


def test_plot_water_levels():
    stations = build_station_list()
    stations_greatest_level_current=stations_highest_rel_level(stations,10)

    names_stations=[]
    for station in stations_greatest_level_current:
        names_stations.append(station[0])
    assert len(names_stations) == 10
    