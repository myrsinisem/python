from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list , update_water_levels
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_station_data
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit

stations = build_station_list()


station=stations[0]
dt = 2
dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
poly, dx=polyfit(dates,levels, 4)
assert isinstance(dx, int)
