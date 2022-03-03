import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import numpy as np
from floodsystem.analysis import polyfit
import matplotlib.dates as date
from floodsystem.station import MonitoringStation


def plot_water_levels(station,dates,levels):
    plt.plot(dates,levels)
    plt.xlabel('date')
    plt.ylabel('water level')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(y = station.typical_range[0], color = "green")
    plt.axhline(y = station.typical_range[1], color = "red")
    plt.tight_layout()
    plt.show()


#def plot_water_level_with_fit(station, dates, levels, p):
    #dates_as_num=plt.dates.date2num(dates)
    #a=dates_as_num[0]#
    #dates2=()
    #for i in dates_as_num:
     #   j=i-a
      #  dates2.append(j)
    #poly, dt=polyfit(dates, levels, p)
    # Plot original data points
    #plt.plot(dates2, levels, '.')

    # Plot polynomial fit at 30 points along interval
    #x1 = np.linspace(dates2[0], dates2[-1], 30)
    #plt.plot(x1, poly(x1))
    
    #plt.title(station.name)
    # Display plot
    #plt.show()

    #poly, dt = polyfit(dates,levels, p)
    #plt.plot(dates,np.polyval(poly, (date.date2num(dates) - )), color='blue')
    #plt.plot(date.date2num(dates),levels, color='black')
    #plt.axhline(y = station.get_typicalRange()[0], color = "green")
    #plt.axhline(y = station.get_typicalRange()[1], color = "red")
    #plt.xlabel("date")
    #plt.ylabel("water level")
    #plt.xticks(rotation=90)
    #plt.tight_layout()
    #plt.title(station.get_stationName())
    #plt.legend(["Polynomial fit", "Data levels", "Typical Low", "Typical High"])
    #plt.show()