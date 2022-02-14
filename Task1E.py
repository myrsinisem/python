from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

"""stations = build_station_list()
print(rivers_by_station_number(stations,10))"""

def run():
    'build a list of stations'
    stations = build_station_list()
    'use rivers_by_station_number to return a list of N rivers in order of most to least stations'
    print('9 rivers with the most stations')
    print(rivers_by_station_number(stations,9))
if __name__ == '__main__':
    run()

