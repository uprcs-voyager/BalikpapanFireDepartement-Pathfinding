import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx
import pandas as pd

# mengatur bagaimana data akan ditampilkan
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 10000)
pd.set_option('display.max_colwidth', None)

# ==== mengambil file graph ml yang sudah dibuat tadi
G = ox.load_graphml("Balikpapan_map_graph.graphml")
# mengubah data yang ada di G menjadi GeoDataFrames 
nodes, edges = ox.graph_to_gdfs(G)
# memplotting graph
# ox.plot_graph(G)
# menampilkan data yang ada pada edges (namun hanya column nya saja)
print("Available data columns: ", edges.columns)


# Menampilkan Nodes (persimpangan) (50) beserta dengan attribute nya 
print("Nodes GeoDataFrame head:")
print(nodes.head(50))
print()
print()
# Menampilkan edges (jalanan) beserta dengan semua attribute kecuali geometry
print("edges GeoDataFrame head :")
print(edges.drop(columns=['geometry']).head(20))
print()
print()
# menampikkan edges (jalanan) beserta dengan attribute di dalam columnsToShow
columnsToShow = ['name', 'highway', 'length', 'maxspeed', 'lanes', 'oneway', 'width', 'junction', 'bridge', 'access']
print("edges GeoDataFrame head with specific columns: ")
pd.set_option('display.max_rows', None)
print(edges[columnsToShow].head(50))
