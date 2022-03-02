from datetime import datetime


import datetime
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations_greatest_level_current=stations_highest_rel_level(stations,10)

    #adding only the name of the station into the list
    names_stations=[]
    for station in stations_greatest_level_current:
        names_stations.append(station[0])
    
    dates=[]
    levels=[]
    for station in names_stations:
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=10))
        plot_water_levels(station,dates,levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()


