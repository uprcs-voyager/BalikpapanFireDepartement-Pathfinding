import heapq
import osmnx as ox
import matplotlib.pyplot as plt
import folium
import contextily as cx
import pandas as pd
import random
from components.creating_nodes import createNo, neighbour
from components.helper import calculateHeuristic_length, get_neighbor_length, reconstruct_path, calculateHeuristic_time, get_neighbor_cost_time
from numpy import sin, cos, arccos, pi, round
from typing import List, Tuple, Dict, Set

G = ox.load_graphml("Balikpapan_map_graph.graphml")
nodes, edges = ox.graph_to_gdfs(G)


def find_path(start_id: Tuple[int], goal_id: Tuple[int], start_coordinate: Tuple[float, float],  goal_coordinate: Tuple[float, float]) -> List[Tuple[float]] :
    # Initializing start node 
    start_node = {
        'id' : start_id,
        'position' : start_coordinate, 
        'g' : 0,
        'h' : calculateHeuristic_time(start_coordinate, goal_coordinate),
        'parent' : None
    }
    start_node['f'] = start_node['g'] + start_node['h']
    # start_node_data = start_node[1]


    # initialize open and closed sets
    open_list = [(start_node['f'], start_id)]
    open_dict = {start_id: start_node}
    closed_set = set()

    while open_list : 
        # Getting the node with the lowest f value
        current_f, current_id = heapq.heappop(open_list)
        current_node = open_dict[current_id]

        # checking have reached the goal yet?
        if current_id == goal_id :
            # DEBUGGING
            # print(f"The current ID is = {current_id} and the goal ID is = {goal_id}")
            current_id = current_id
            goal_id = goal_id
            final_path = reconstruct_path(current_node)
            return final_path, closed_set

        closed_set.add(current_id)

        # explore neighbor
        for neighbor_pos in get_neighbor_cost_time(current_id) :
            neighbor_id = neighbor_pos['neighbor']
            edge_time = neighbor_pos['time']

            if neighbor_id in closed_set : 
                continue
            # Calculating new path cost
            tentative_g = current_node['g'] + edge_time
            neighbor_latitude = G.nodes[neighbor_id]['y']
            neighbor_longitude = G.nodes[neighbor_id]['x']
            neighbor_coordinates = (neighbor_latitude, neighbor_longitude)
            h_score = calculateHeuristic_time(neighbor_coordinates, goal_coordinate)
            f_score = tentative_g + h_score

            if neighbor_id not in open_dict :
                neighbor_id = neighbor_pos['neighbor']
                neighbor_latitude = G.nodes[neighbor_id]['y']
                neighbor_longitude = G.nodes[neighbor_id]['x']
                neighbor_coordinates = (neighbor_latitude, neighbor_longitude)
                neighbor = neighbour(
                    id = neighbor_id, 
                    position = neighbor_pos,
                    g = tentative_g, 
                    h = calculateHeuristic_time(neighbor_coordinates, goal_coordinate),
                    parent = current_node
                )
                heapq.heappush(open_list, (neighbor['f'], neighbor_id))
                open_dict[neighbor_id] = neighbor

            elif tentative_g < open_dict[neighbor_id]['g'] : 
                # Found a better path to the neighbor 
                neighbor = open_dict[neighbor_id]
                neighbor['g'] = tentative_g
                neighbor['f'] = tentative_g + neighbor['h']
                neighbor['parent'] = current_node
                heapq.heappush(open_list, (neighbor['f'], neighbor_id))
                open_dict[neighbor_id] = neighbor

# no path found
    return[] 

