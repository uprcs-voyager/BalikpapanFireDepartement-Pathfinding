# Timeline of the projects
## Algorithm used
The algorithm used for this pathfinding project is A*
- G Cost = Distance from the starting node
- H Cost (heuristic) = Distance from end node 
- F Cost = G Cost + F cost  
## Preparing the data
- getting the balikpapan map using osmnx
- Downloading the balikpapan graphml to speed up runtime by being getting the graphml data locally 
- Inspecting available data for the nodes and edges
- Seeing what kinds of 'data' there is on the nodes and edges for example like (how many roads are connected to a node, what attribute each edges have etc..)

## Making 'part' of the heuristic function (6/12/2025)
the g_and_heuristic_cost file inside the the testing folder is composed of codes that give a little snippet of the avalaible data and nodes, the math formula, codes that pick 2 random nodes and then giving the distance between those 2 nodes. It works by using the haversine formula by using the latitude and longutide from both respected node to determine the distance between them. the output given is accurate and proven by google earth checking.

## 'Seeing' What neighbor a node have 
the codes inside available_neighbours_and_their_distance.py are used to find available neighbor that node 1 ( the starting node) and node 2 (the end node) has. The codes also give all the neighbor edges length so it will be usefull for the next step, which is creating the A* algorithm 

## 'Splitting' the codes to improve readability (7/12/2025)
The current progress is i made a function inside creating_nodes.py that will generate the starting and the end node based on the argument given to it and making codes for calculating and seeing what are the available neighbor nodes are inside the helper.py so hopefully the flow be like :
1. Creating a node using the createNode function and the parameters are type (1/2) becuase : 
   -   position or the starting position is already assigned if the type is 1, the g is set to 0 and to get the h we need to call the calculate heuristic function which will take 2 parameters (position and goal)

2. The current plan to set the goal is to call the create node function again but the type parameters will be 2 (which means the node that will be created is the target node)

3. based on those 2 nodes the next steps will be to calculate the heuristic by calling the calculate heurisctic function that will take 2 parameters (start and goal)

4. Work In Progress

'