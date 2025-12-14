# External libraries
print("importing..")
import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx
import pandas as pd
import random
print("dependencies..")
from numpy import sin, cos, arccos, pi, round
# Internal Import
import components
from components import aSTAR, creating_nodes, helper, fire_station
from components.fire_station import get_fire_stations_nodes, get_closest_fire_station_to_target, fire_station





print("starting")
# start_pos = creating_nodes.createNo(type=1)
# start_pos_data = start_pos[1]
# start_pos_id = start_pos_data['id']
# start_pos_coordinate = start_pos_data['position']
# print(f"start Pos ID: {start_pos_id}")
# print(start_pos)



# Creating the goal node
print()
goal_pos = creating_nodes.createNo(type=2)
goal_pos_data = goal_pos[1]
goal_pos_id = goal_pos_data['id']
goal_pos_coordinate = goal_pos_data['position']
print(f"goal Pos ID: {goal_pos_id}")
print(goal_pos)



# Choosing the nearest fire station corresponding to the goal
G = ox.load_graphml('Balikpapan_map_graph.graphml')
fire_station_nodes = get_fire_stations_nodes(G, fire_station)
# debugging
print(f"\nFound {len(fire_station_nodes)} fire station :  ")
for name in fire_station_nodes.keys() :
    print(f" - {name}")
closest_fire_station_to_target = get_closest_fire_station_to_target(goal_pos_coordinate, fire_station_nodes, G)
start_id = closest_fire_station_to_target['node_id']
start_coordinate = (G.nodes[start_id]['y'], G.nodes[start_id]['x'])




print(start_coordinate)
print(goal_pos_coordinate)

print(f"emergency was found in : {goal_pos_coordinate}")
print(f"The nearest fire station choosen is: {closest_fire_station_to_target['name']} || with the distance of {closest_fire_station_to_target['distance']/1000:.2f} KM to the target")

path = aSTAR.find_path(start_id, goal_pos_id, start_coordinate, goal_pos_coordinate)



























# print("========================================================================Partial Data Inspection==============================================================================================")
# print()
# G = ox.load_graphml("Balikpapan_map_graph.graphml")
# nodes, edges = ox.graph_to_gdfs(G)
# print("Available data columns: ", edges.columns)
# print("========================================================")
# print()
# print("========================================================")
# print("Nodes GeoDataFrame head:")
# print(nodes.head(5))
# print()
# print()
# print("========================================================")
# columnsToShow = ['name', 'highway', 'length', 'maxspeed', 'lanes', 'oneway', 'width', 'junction', 'bridge', 'access']
# print("edges GeoDataFrame head with specific columns: ")
# print(edges[columnsToShow].head(5))
# print()
# print("=========================================================================Partial Data Inspection======================================================================================================")
# print("\n\n\n\n\n\n\n\n")

# def rad_to_degree(radians) :
#     degrees = radians * 180 / pi
#     return degrees

# def degree_to_rad(degrees) :
#     radians = degrees * pi /180
#     return radians

# def getDistanceBetweenTwoPoints(latitude1, longitude1, latitude2, longitude2) :
#     theta  = longitude1 - longitude2
#     distance  = 60 * 1.1515 * rad_to_degree(
#         arccos(
#         (sin(degree_to_rad(latitude1)) * sin(degree_to_rad(latitude2))) + 
#         (cos(degree_to_rad(latitude1)) * cos(degree_to_rad(latitude2)) * cos(degree_to_rad(theta)))
#     )
#     )

#     return round(distance * 1609.34, 2)

# def gettingNeighborLength(node) :
#     for v in G.neighbors(node) : 
#         for key, data in G.get_edge_data(node, v).items() :
#             node_data = G.nodes[node]
#             edge_lenght = data['length']
#             # node_latitude = node_data['y']
#             # node_longitude = node_data['x']
#             print(f"Jarak dari node {node}  ke node {v} dengan key = {key} adalah {edge_lenght:.2f} Meter ")



# # ====================================== NODE 1 DATA =====================================
# # Mengambil node pertama secara random dari list node yang ada 
# # Node1 akan menjadi titik mulai
# node_ids = list(G.nodes())
# node1 = random.choice(node_ids)
# node1_data = G.nodes[node1]
# node1_latitude = node1_data['y']
# node1_longitude = node1_data['x']
# node1_id = node1
# # seeing available neighbor for node 1 
# neighborsN1 = list(G.neighbors(node1))
# # getting the neighbor lenght
# # for v1 in G.neighbors(node1) : 
# #     for key1, data1 in G.get_edge_data(node1, v1).items() :
# #         edge1_lenght = data1['lenght']
# #         print(f"Jarak dari node {node1} ke node {v1} dengan key = {key1} adalah {edge1_lenght:.2f} Meter")
# # ====================================== NODE 1 DATA =====================================


# # ====================================== NODE 2 DATA =====================================
# # Mengambil node kedua secara random dari list node yang ada
# # Node kedua akan menjadi titik mulai 
# node2 = random.choice(node_ids)
# node2_data = G.nodes[node2]
# node2_latitude = node2_data['y']
# node2_longitude = node2_data['x']
# node2_id = node2
# # seeing available neighbor for node 2 
# neighborsN2 = list(G.neighbors(node2))
# # ====================================== NODE 2 DATA =====================================


# print("===============================================================================The Main Content=================================================================================================================")
# print()
# print(f"Node 1 yang terpilih memiliki ID = || {node1} || dengan data  {node1_data} || latitude = {node1_latitude}, longitude = {node1_longitude}")
# print(f"Node 2 yang terpilih memiliki ID = || {node2} || dengan data  {node2_data} || latitude = {node2_latitude}, longitude = {node2_longitude}")
# jarak_antara_start_end  = getDistanceBetweenTwoPoints(node1_latitude, node1_longitude, node2_latitude, node2_longitude)
# jarak_antara_start_end_KM = round(jarak_antara_start_end * 0.001, 2)
# print(f"Jarak antara node 1 yang memiliki ID {node1_id} dan node 2 yang memiliki id {node2_id} adalah : {jarak_antara_start_end} Meter  / {jarak_antara_start_end_KM} KM")


# # ====================================== NODE 1 & 2 Neighbors =====================================
# print(f"\nBerikut adalah daftar tetangga yang tersedia pada node 1 : {neighborsN1}\nBerikut adalah daftar tetangga yang tersedia pada node 2 : {neighborsN2} ")
# print()
# print("Berikut adalah jarak antar node yang tersedia\n ")
# print("Node Awal (Starting Node): ")
# node1NeighborLength = gettingNeighborLength(node1)
# print()
# print("Node Akhir (Final Node): ")
# node2NeighborLength = gettingNeighborLength(node2)



















print("\n\n\n\n")


