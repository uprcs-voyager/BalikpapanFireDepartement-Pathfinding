import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx


# ==== mengambil file graph ml yang sudah dibuat tadi
G = ox.load_graphml("Balikpapan_map_graph.graphml")
# mengubah data yang ada di G menjadi GeoDataFrames 
nodes, edges = ox.graph_to_gdfs(G)
# memplotting graph
ox.plot_graph(G)
# menampilkan data yang ada pada edges (namun hanya column nya saja)
print("Available data columns: ", edges.columns)