import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx
import pandas as pd
import random
from numpy import sin, cos, arccos, pi, round



G = ox.load_graphml("Balikpapan_map_graph.graphml")
nodes, edges = ox.graph_to_gdfs(G)
print("Available data columns: ", edges.columns)
print("========================================================")
print()
print("========================================================")
print("Nodes GeoDataFrame head:")
print(nodes.head(5))
print()
print()
print("========================================================")
columnsToShow = ['name', 'highway', 'length', 'maxspeed', 'lanes', 'oneway', 'width', 'junction', 'bridge', 'access']
print("edges GeoDataFrame head with specific columns: ")
print(edges[columnsToShow].head(5))
print("========================================================")


def rad_to_degree(radians) :
    degrees = radians * 180 / pi
    return degrees

def degree_to_rad(degrees) :
    radians = degrees * pi /180
    return radians

def getDistanceBetweenTwoPoints(latitude1, longitude1, latitude2, longitude2) :
    theta  = longitude1 - longitude2
    distance  = 60 * 1.1515 * rad_to_degree(
        arccos(
        (sin(degree_to_rad(latitude1)) * sin(degree_to_rad(latitude2))) + 
        (cos(degree_to_rad(latitude1)) * cos(degree_to_rad(latitude2)) * cos(degree_to_rad(theta)))
    )
    )

    return round(distance * 1609.34, 2)



# Mengambil node pertama secara random dari list node yang ada 
# Node1 akan menjadi titik mulai
node_ids = list(G.nodes())
node1 = random.choice(node_ids)
node1_data = G.nodes[node1]
node1_latitude = node1_data['y']
node1_longitude = node1_data['x']
node1_id = node1

# Mengambil node kedua secara random dari list node yang ada
# Node kedua akan menjadi titik mulai 
node2 = random.choice(node_ids)
node2_data = G.nodes[node2]
node2_latitude = node2_data['y']
node2_longitude = node2_data['x']
node2_id = node2
print()
print(f"Node 1 yang terpilih memiliki ID = || {node1} || dengan data  {node1_data} || latitude = {node1_latitude}, longitude = {node1_longitude}")
print(f"Node 2 yang terpilih memiliki ID = || {node2} || dengan data  {node2_data} || latitude = {node2_latitude}, longitude = {node2_longitude}")
jarak_antara_start_end  = getDistanceBetweenTwoPoints(node1_latitude, node1_longitude, node2_latitude, node2_longitude)
jarak_antara_start_end_KM = round(jarak_antara_start_end * 0.001, 2)
print(f"Jarak antara node 1 yang memiliki ID {node1_id} dan node 2 yang memiliki id {node2_id} adalah : {jarak_antara_start_end}Meter  / {jarak_antara_start_end_KM} KM")




