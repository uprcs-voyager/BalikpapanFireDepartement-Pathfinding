import osmnx as ox 
import matplotlib.pyplot as plt
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
from components import aSTAR, creating_nodes, helper
from components.initialization import path


G = ox.load_graphml('Balikpapan_map_graph.graphml')

hasil_pencarian = path

if hasil_pencarian :
    final_path = hasil_pencarian[0]
    closed_set = hasil_pencarian[1]
else : 
    print("Something is wrong")

G_explored = G.subgraph(closed_set)

abandoned_nodes = list(closed_set - set(final_path))

figure, ax = ox.plot_graph(
    G, 
    show= False, 
    close= False, 
    edge_color="#5E5E5E", 
    edge_linewidth=1,
    node_size=0,
    bgcolor='black',
    figsize=(24,24)
)

ox.plot_graph(
    G_explored, 
    ax=ax,
    show=False, 
    close=False, 
    edge_color='#F4D03F',
    edge_linewidth=0.3, 
    node_size=0
)


# abandoned_nodes_x = []
# abandoned_nodes_y = []

# if abandoned_nodes : 
#     for node in abandoned_nodes : 
#         koordinat_x = G.nodes[node]['x']
#         abandoned_nodes_x.append(koordinat_x)

#     for node in abandoned_nodes : 
#         koordinat_y = G.nodes[node]['y']
#         abandoned_nodes_y.append(koordinat_y)
# ax.scatter(abandoned_nodes_x, abandoned_nodes_y, c='red', s=15, alpha=0.6, label='abandoned/explored', zorder=2)


total_time = 0
total_distance = 0

for i in range (len(final_path)-1) :
    u, v = final_path[i], final_path[i+1]
    edge_data = G.get_edge_data(u,v)[0]

    distance = edge_data['length']
    speed_mps = helper.get_speed_from_edges(edge_data)
    time = distance/speed_mps

    total_time += time
    total_distance += distance

print(f"Total time: {total_time/60:.2f} Minutes")
print(f"Total distance : {total_distance/1000:.2f} KM")



if final_path :
    ox.plot_graph_route(
        G, 
        final_path,
        route_color='green', 
        route_linewidth=4, 
        route_alpha=1.0, 
        orig_dest_size=100, 
        ax=ax
    )

plt.show()

