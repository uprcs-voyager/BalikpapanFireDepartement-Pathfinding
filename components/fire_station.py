import heapq
import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx
import pandas as pd
import random
from components.creating_nodes import createNo, neighbour
from components.helper import calculateHeuristic_length, get_neighbor_length, reconstruct_path, calculateHeuristic_time, get_neighbor_cost_time
from numpy import sin, cos, arccos, pi, round
from typing import List, Tuple, Dict, Set


fire_station = {
    'Pos pemadam kebakaran balikpapan tengah' : {
        'latitude' : -1.2627928,
        'longitude' : 116.8430227,
        'address' : ' PRPV+W64 depan gajah mada Jl. Mayjend Sutoyo Klandasan Ilir Kec. Balikpapan Kota, Kota Balikpapan, Kalimantan Timur 76113'
    },
    'Pos BPBD WIL UTARA Kota Balikpapan' : {
        'latitude' : -1.2369282,
        'longitude' : 116.8401686,
        'address' : 'Jl. Soekarno Hatta No.1, Gn. Samarinda, Kec. Balikpapan Utara, Kota Balikpapan, Kalimantan Timur 76123'
    },
    'pos pemadam kebakaran uptbd balikpapan selatan' : {
        'latitude' : -1.242757,
        'longitude' : 116.8930373,
        'address' : 'Sepinggan, Balikpapan Selatan, Balikpapan City, East Kalimantan'
    },
    'Pos Pemadam Kebakaran, Uptpbd Wil Timur' : {
        'latitude' : -1.2226804,
        'longitude' : 116.9697158,
        'address' : 'Jl. Lumba - Lumba, Manggar Baru, Kec. Balikpapan Tim., Kota Balikpapan, Kalimantan Timur'
    },
    'pemadam kebakaran kebun sayur' : {
        'latitude' : -1.2340732,
        'longitude' : 116.8250995,
        'address' : 'Baru Ilir, Balikpapan Barat, Balikpapan City, East Kalimantan'
    },
    'Pos Pemadam UPT PBD Wil Kota' : {
        'latitude' : -1.2697652,
        'longitude' : 116.8341792,
        'address' : 'Jl. Kapten Piere Tendean No.60, Gunungsari Ilir, Kec. Balikpapan Tengah, Kota Balikpapan'
    }
}

def get_fire_stations_nodes(G, fire_station) :
    station_nodes = {}

    for name, data in fire_station.items() :
        nearest_node = ox.distance.nearest_nodes(
            G, 
            X = data ['longitude'],
            Y = data ['latitude']
        )
    
        station_nodes[name] = {
            'node_id' : nearest_node,
            'y_coordinates' : data['latitude'],
            'x_coordinates' : data['longitude'],
            'coordinates' : (data['latitude'], data['longitude']),
            'address' : data['address']
        }

    return station_nodes

def get_closest_fire_station_to_target(target_coordinates, station_nodes, G) :
    minimal_distance = float('inf')
    closest_station = None

    for name, data in station_nodes.items() :
        node_id = data['node_id']
        node_coordinates = (G.nodes[node_id]['y'], G.nodes[node_id]['x'])   
        distance = calculateHeuristic_length(node_coordinates, target_coordinates)

        if distance < minimal_distance :
            minimal_distance = distance
            closest_station = {
                'name' : name, 
                'node_id' : node_id,
                'distance' : distance
            }
    
    return closest_station
    