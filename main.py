import osmnx as ox 
import matplotlib.pyplot as plt
# print("importing..")
import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx
import pandas as pd
import random
# print("dependencies..")
from numpy import sin, cos, arccos, pi, round
# Internal Import
import components
from components import aSTAR, creating_nodes, helper
from components.initialization import path, start_id, goal_pos_id, closest_fire_station_to_target
from components.helper import getting_taken_road_info


G = ox.load_graphml('Balikpapan_map_graph.graphml')

hasil_pencarian = path
if hasil_pencarian :
    final_path = hasil_pencarian[0]
    closed_set = hasil_pencarian[1]
else : 
    print("Something is wrong")

# ====== KODE UNTUK MENEUNJUKAN NODE YANG TIDAK DIGUNAKAN =========================

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

# ====== KODE UNTUK MENEUNJUKAN NODE YANG TIDAK DIGUNAKAN =========================








# ================== Setting tampilan graph =========================================
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


start_x = G.nodes[start_id]['x']
start_y = G.nodes[start_id]['y']
goal_x = G.nodes[goal_pos_id]['x']
goal_y = G.nodes[goal_pos_id]['y']

# Adding start marker whcih is the fire station
ax.scatter(start_x, start_y, c='orange', s=400, marker='.', edgecolors='white', linewidths=1, zorder=10, label='Fire Station')

# Adding goal marker whcih is the emergency location
ax.scatter(goal_x, goal_y, c='red', s=400, marker='.', edgecolors='white', linewidths=1, zorder=10, label='Emergency')

# Menambahkan text label 
# Label statsiun kebakaran
station_name = closest_fire_station_to_target['name']
ax.text(start_x, start_y, f'\n{station_name}', fontsize=10, ha='center', color='white', bbox=dict(boxstyle='round', facecolor='orange', alpha=0.7))
# label lokasi emergency
ax.text(goal_x, goal_y, '\nEmergency Location', fontsize=10, ha='center', color='white', bbox=dict(boxstyle='round', facecolor='red', alpha=0.7))
ax.legend(loc='upper right', fontsize=12)
# ================== Setting tampilan graph =========================================







# ================================= Mendapatkan data total jarak yang ditempuh dan waktu yang dihabiskan pada suatu rute yag telah dipilih ===============
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
# ================================= Mendapatkan data total jarak yang ditempuh dan waktu yang dihabiskan pada suatu rute yag telah dipilih ===============







# =============================== Menampilkan nama-nama jalan yang telah/harus di ambil berdasarkan rute yang dipilih =============
instruction = getting_taken_road_info(final_path, G)
current_road = None
route_steps = 0
print("===== HARAP IKUTI PANDUAN JALAN INI =====")
for i in instruction : 
    road = i['road']
    if road != current_road :
        if current_road is not None:
            print(f"\n{route_steps}. Follow {current_road}")


        current_road = road
        route_steps += 1

if current_road is not None : 
    print(f"\n{route_steps}. Follow {current_road}")

print()
print()
print("===== INFO MENGENAI WAKTU DAN JARAK DARI RUTE YANG TELAH DIPILIH =====")
print(f"Total time: {total_time/60:.2f} Minutes")
print(f"Total distance : {total_distance/1000:.2f} KM")
print()
print()
# =============================== Menampilkan nama-nama jalan yang telah/harus di ambil berdasarkan rute yang dipilih =============













# ==================== MENAMPILKAN GAMBAR BERISI RUTE YANG DIPILIH ================================
if final_path :
    ox.plot_graph_route(
        G, 
        final_path,
        route_color='green', 
        route_linewidth=4, 
        route_alpha=1.0, 
        orig_dest_size=100, 
        ax=ax,
    )




# ================= Menampilkan title-title agar plot lebih informatif ========================
title_text = f"Rute Departemen Pemadam kebakaran menuju lokasi emergency dengan menggunakan Algoritma A*\n"
title_text += f"Dari: {closest_fire_station_to_target['name']}\n"
title_text += f"Total Jarak Tempuh: {total_distance/1000:.2f} KM\n"
title_text += f"Total Waktu Dihabiskan: {total_time/60:.2f} Minutes\n"
ax.set_title(title_text, fontsize=12, color='green')
# ================= Menampilkan title-title agar plot lebih informatif ========================

plt.show()
# ==================== MENAMPILKAN GAMBAR BERISI RUTE YANG DIPILIH ================================

