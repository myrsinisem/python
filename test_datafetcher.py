# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the stationdata module"""

import datetime
from datetime import date
#from xml.dom.xmlbuilder import _DOMInputSourceCharacterStreamType

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch
import dateutil.parser


def test_build_station_list():

    # Build list of stations
    stations = build_station_list()

    # Find station 'Cam'
    for station in stations:
        if station.name == 'Cam':
            station_cam = station
            break

    # Assert that station is found
    assert station_cam

    # Fetch data over past 2 days
    dt = 2
    dates2, levels2 = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    assert len(dates2) == len(levels2)

    # Fetch data over past 10 days
    dt = 10
    dates10, levels10 = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    assert len(dates10) == len(levels10)
    assert len(dates10) > len(levels2)

def test_fetch_measure_levels():
    stations = build_station_list

    a = datetime.datetime(2022,3,2)

    now =datetime.datetime.utcnow()

    assert now.strftime('%m') == a.strftime('%m') 














