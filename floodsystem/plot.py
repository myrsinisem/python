import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit


def plot_water_levels(station,dates,levels):
    plt.plot(dates,levels)
    plt.xlabel('date')
    plt.ylabel('water level')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    dates_as_num=plt.dates.date2num(dates)
    a=dates_as_num[0]#
    dates2=()
    for i in dates_as_num:
        j=i-a
        dates2.append(j)
    poly, dt=polyfit(dates, levels, p)
    # Plot original data points
    plt.plot(dates2, levels, '.')

    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(dates2[0], dates2[-1], 30)
    plt.plot(x1, poly(x1))
    
    plt.title(station.name)
    # Display plot
    plt.show()