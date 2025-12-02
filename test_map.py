import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx

# mendefinisikan tempat yang ingin diambil datanya
PLACE_NAME = 'Balikpapan, Indonesia'
# mengambil data berdasarkan PLACE_NAMe
G = ox.graph_from_place(PLACE_NAME, network_type='drive')
# ox.plot_graph(G)

# mengubah data yang ada di G menjadi GeoDataFrames 
nodes, edges = ox.graph_to_gdfs(G)

# memvisualiasikan data (overlapping antara map dengan edges G)
m = edges.explore(color="red", tiles="CartoDB positron")

m.save("Balikpapan_map.html")

# menampilkan data yang ada pada edges (namun hanya column nya saja)
print("Available data columns: ", edges.columns)