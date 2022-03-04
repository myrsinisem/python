from floodsystem.stationdata import build_station_list
from floodsystem.geo import towns_with_station
from floodsystem.geo import stations_by_town
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
towns = towns_with_station(stations)


stationsByTown = stations_by_town(stations)
tol=0.9
update_water_levels(stations)
stations_high=stations_level_over_threshold(stations, tol)
sta_high=[]
for station in stations_high:
    sta_high.append(station[0].name)
tol=0.8
stations_medium=stations_level_over_threshold(stations, tol)
sta_medium=[]
for station in stations_medium:
    sta_medium.append(station[0].name)
tol=0.7
stations_low=stations_level_over_threshold(stations, tol)
sta_low=[]
for station in stations_low:
    sta_low.append(station[0].name)
risk=[]
for town in stationsByTown:
    total=0
    for station in stationsByTown[town]:
        if station in sta_high:
           total+=3
        elif station in sta_medium:
            total+=2
        elif station in sta_low:
            total+=1
    average=total/len(stationsByTown[town])
    if average>2.7:
        x=[town, ":severe"]
        risk.append(x)
    elif average>2:
        x=[town, ":high"]
        risk.append(x)
    elif average>1:
        x=[town, ":moderate"]
        risk.append(x)
    elif average>0.5:
        x=[town, ":low"]
        risk.append(x)

print (risk)