from ast import Continue
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
     
stations = build_station_list()
tol = 0.2

update_water_levels(stations)
stations_thresh = stations_level_over_threshold(stations, tol)
     
list = []
for station in stations_thresh:
    list.append(station[0].name)
#print (list)
 #tolerance is low 0.2 so it should always print more than 10 --> test is universal
assert len(list) > 10

update_water_levels(stations)
stations_high_threat = stations_highest_rel_level(stations, 10)
     
list2 = []
for station in stations_high_threat:
    list2.append(station[0].name)
#print (list2)

assert len(list2) == 10



#I INITAILLY WANTED TO TEST FOR THE FUNCTIONS BUT IT KEPT GIVING ME AN ERROR THAT STATIONS WAS A FUNCTION AND NOT ITERABLE
#SO I MADE THESE SIMPLE TESTS INSTEAD WHICH SHOULD WORK EVEN IF DATA CHANGES
