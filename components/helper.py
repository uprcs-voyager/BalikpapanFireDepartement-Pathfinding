import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx
import pandas as pd
import random
from numpy import sin, cos, arccos, pi, round
from typing import List, Tuple, Dict, Set

def rad_to_degree(radians) :
    degrees = radians * 180 / pi
    return degrees

def degree_to_rad(degrees) :
    radians = degrees * pi /180
    return radians

G = ox.load_graphml("Balikpapan_map_graph.graphml")
nodes, edges = ox.graph_to_gdfs(G)

def calculateHeuristic(pos1: Tuple[float, float], pos2: Tuple[float, float]) -> float :
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

def gettingNeighbor (node) :
    neighbor = list(G.neighbors(node))
    return neighbor

def get_neighbor_length(id: Tuple[float]) -> List[Tuple[float]] :
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


def reconstruct_path (goal_node: Dict) -> List[Tuple[float]] :
    path = []
    current = goal_node
    while current is not None :
        path.append(current['id'])
        current = current['parent']

    return path[::-1]
