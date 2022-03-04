import numpy as np

from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.station import MonitoringStation
import matplotlib.dates as date

def test_plot_water_levels():
    
    #creating internal data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (1.0, 1.0)
    trange = (0.5, 1.0)
    river = "River"
    town = "Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.set_latestLevel(1)
    y = [0,1,2,3,4,5]
    x = y
    plot_water_levels(s,x,y)
    np.testing.assert_array_equal(y,x)
