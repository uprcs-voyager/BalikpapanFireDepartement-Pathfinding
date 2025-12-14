import osmnx as ox
import pandas as pd


filename = 'Balikpapan_map_graph.graphml' 

print(f"Sedang mengaudit isi file: {filename} ...")
G = ox.load_graphml(filename)


edges = ox.graph_to_gdfs(G, nodes=False, edges=True)


print("\n--- JENIS JALAN YANG DITEMUKAN ---")
print(edges['highway'].value_counts())