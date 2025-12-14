import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx
import pandas as pd
import random
from numpy import sin, cos, arccos, pi, round
from typing import List, Tuple, Dict, Set


default_speed_KM = {
        'motorway': 100,
        'trunk': 80,
        'primary': 50,
        'secondary': 40,
        'tertiary': 30,
        'residential': 30,
        'living_street': 10,
        'unclassified': 20,
    }
# diubah ke meter per detik
GLOBAL_MAX_SPEED_MPS = 90 / 3.6


def rad_to_degree(radians) :
    degrees = radians * 180 / pi
    return degrees

def degree_to_rad(degrees) :
    radians = degrees * pi /180
    return radians

G = ox.load_graphml("Balikpapan_map_graph.graphml")
nodes, edges = ox.graph_to_gdfs(G)

def calculateHeuristic_length(pos1: Tuple[float, float], pos2: Tuple[float, float]) -> float :
    latitude1, longitude1 = pos1
    latitude2, longitude2 = pos2
    theta = longitude1 - longitude2
    distance  = 60 * 1.1515 * rad_to_degree(
        arccos(
        (sin(degree_to_rad(latitude1)) * sin(degree_to_rad(latitude2))) + 
        (cos(degree_to_rad(latitude1)) * cos(degree_to_rad(latitude2)) * cos(degree_to_rad(theta)))
    )
    )
    # the returned value will be in meters
    return round(distance * 1609.34, 2)


def calculateHeuristic_time(pos1: Tuple[float, float], pos2: Tuple[float, float]) -> float :
    distance_in_meter = calculateHeuristic_length(pos1, pos2)
    # the returned value will be in meters
    return distance_in_meter/GLOBAL_MAX_SPEED_MPS


def get_speed_from_edges(edge_data: Dict) -> float :
    maxspeed = edge_data.get('maxspeed', 'None')
    highway = edge_data.get('highway', 'unclassified')
    
    if maxspeed is not None and str(maxspeed).lower() != 'nan' :
        if isinstance(maxspeed, list) :
            maxspeed = maxspeed[0]
        try :
            speed_kmh = float(str(maxspeed).split()[0])
            return speed_kmh / 3.6
        except : 
            pass

 
    if isinstance(highway, list) :
        highway = highway[0]
    speed_kmh = default_speed_KM.get(highway, 20)

    # konversi ke meter/second
    return speed_kmh/3.6

def get_neighbor_cost_time(node_id) :
    neighbor_list = []
    for neighbor_id in G.neighbors(node_id) :
        for key, data in G.get_edge_data(node_id, neighbor_id).items() :
            edge_length = data['length']
            edge_speed = get_speed_from_edges(data)
            edge_time_cost = edge_length  / edge_speed

            neighbor_cost_time_data = {
                'neighbor' : neighbor_id,
                'key' : key, 
                'speed' : edge_speed,
                'length' : edge_length,
                'time' : edge_time_cost
            }
            neighbor_list.append(neighbor_cost_time_data)
    return neighbor_list

def gettingNeighbor (node) :
    neighbor = list(G.neighbors(node))
    return neighbor

def get_neighbor_length(id: Tuple[int]) -> List[Tuple[int]] :
    neighbor_list = []
    for v in G.neighbors(id) :
        if v != 0 :
            for key, data in G.get_edge_data(id, v).items() :
                edge_length = data['length']
                neighbor_data = {
                    'neighbor' : v,
                    'key' : key,
                    'distance' : edge_length
                }
                neighbor_list.append(neighbor_data)
    return neighbor_list


def reconstruct_path (goal_node: Dict) -> List[Tuple[int]] :
    path = []
    current = goal_node
    while current is not None :
        path.append(current['id'])
        current = current['parent']

    track = path[::-1]
    return track


# =============================== Menampilkan nama-nama jalan yang telah/harus di ambil berdasarkan rute yang dipilih =============
def getting_taken_road_info(path, G) : 
    instruction = []

    for i in range(len(path)-1) :
        u, v = path[i], path[i+1]
        # take edge data
        edge_data = G.get_edge_data(u, v)
        if edge_data :
            edge_info = edge_data[0]  #getting the first edge
            road_name = edge_info.get('name', 'Unnamed Road') #getting the road names

            if isinstance(road_name, list) :
                road_name = ','.join(str(n) for n in road_name)
            
            # getting distance and speed
            distance = edge_info['length']
            speed = get_speed_from_edges(edge_info)
            time = distance/speed
            distance_speed_data = {
                'segment' : i+1,
                'road' : road_name,
                'distance' : distance,
                'time' : time,
                'start_node' : u,
                'end_node' : v,

            }

            instruction.append(distance_speed_data)
    
    return instruction