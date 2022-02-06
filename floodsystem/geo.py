# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine

from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    'Return a list of tuples using list of stations sorted by distance'
    list=[]
    for station in stations:
        list.append((station.name, station.town,
         haversine(station.coord, p)))
    return sorted_by_key(list, 2, False)

def stations_within_radius(stations,centre,r):
    'Return a list of all stations within radius r of a coordinate x'
    list_radius=[]
    for station in stations:
        if haversine(station.coord, centre) <10:
            list_radius.append(station.name)
    list_radius.sort
    return list_radius

def rivers_with_station(stations):
    'Return a set with the names of the rivers with a monitoring station with no repeats'
    set_river=set()
    for station in stations:
        set_river.add(station.river)
    return set_river

def stations_by_river(stations):
    station_river = {}
    for i in rivers_with_station(stations):
        stationsAtRiver = []
        for station in stations:
            if i == station.river:
                stationsAtRiver.append(station.name)
        station_river.update({i: stationsAtRiver})
    return station_river

