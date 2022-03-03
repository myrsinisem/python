import matplotlib as plt
import numpy as np
import matplotlib.dates as date

def polyfit(dates, levels, p):
    dates_as_num=date.date2num(dates)
    a=dates_as_num[0]
    dates2=()
    for i in dates_as_num:
        j=i-a
        dates2.append(j)
    p_coeff = np.polyfit(dates2, levels, p)
    
    poly = np.poly1d(p_coeff)

    return poly, a

