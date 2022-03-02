import matplotlib as plt
import numpy as np

def polyfit(dates, levels, p):
    dates_as_num=plt.dates.date2num(dates)
    a=dates_as_num[0]#
    dates2=()
    for i in dates_as_num:
        j=i-a
        dates2.append[j]
        
    # Create set of 10 data points on interval (0, 2)
    
    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(dates2, levels, p)
    print (p_coeff)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    print(poly)

    return poly, a

