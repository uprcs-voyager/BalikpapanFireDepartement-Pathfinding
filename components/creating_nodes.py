import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx
import pandas as pd
import random
from numpy import sin, cos, arccos, pi, round
from typing import List, Tuple, Dict, Set
import heapq

G = ox.load_graphml("Balikpapan_map_graph.graphml")
nodes, edges = ox.graph_to_gdfs(G)

def StartingNode(type, g: 0, h: Tuple[float, float], parent: Dict = None) -> Dict :
    node_ids = list(G.nodes())
    if type == 1 : 
        node1 = random.choice(node_ids)
        node1_data = G.nodes[node1]
        node1_latitude = node1_data['y']
        node1_longitude = node1_data['x']
        location = (node1_latitude, node1_longitude)
        node1_id = node1
        data1 = print(f"Node 1 yang terpilih memiliki ID = || {node1_id} || dengan data  {node1_data} || latitude = {node1_latitude}, longitude = {node1_longitude}")
        dict1 = {
            'position' : location,
            'g' : g,
            'h' : h, 
            'f' : g+h, 
            'parent' : parent

        }
        return data1, dict1
    if type == 2 :
        node2 = random.choice(node_ids)
        node2_data = G.nodes[node1]
        node2_latitude = node1_data['y']
        node2_longitude = node1_data['x']
        location2 = (node1_latitude, node1_longitude)
        node2_id = node1
        data2 = print(f"Node 2 yang terpilih memiliki ID = || {node2_id} || dengan data  {node2_data} || latitude = {node2_latitude}, longitude = {node2_longitude}")
        return data2, location2

    else : 
        print("Only use value between 1 and 2")

