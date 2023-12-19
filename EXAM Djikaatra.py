
# Additional Explanation- This code is an implementation of Dijkstra’s shortest path algorithm. 
# It finds the shortest path between a source vertex and all other vertices in a graph.
 
# The code creates a 
# Graph class that has three methods:
    # -  _init_,
#     -  printSolution, 
#      - dijkstra.

# The _init_ method initializes the graph with a given number of vertices. 

# The printSolution method prints the shortest distance from the source vertex to all other vertices.

#  The dijkstra method implements Dijkstra’s algorithm to find the shortest path from the source vertex
#  to all other vertices.

# The graph attribute of the Graph class is a two-dimensional list that represents the adjacency matrix of the graph.
#  The minDistance method is a utility function that finds the vertex with the minimum distance value from the set of vertices not yet included in the shortest path tree. 
# The dijkstra method initializes the distance of all vertices to infinity except the source vertex, which is initialized to 0. It then iteratively selects the unvisited vertex with the smallest tentative distance from the source and visits its neighbors to update their tentative distances if a shorter path is found. This process continues until the destination vertex is reached or all reachable vertices have been visited.

# In this specific example,
#  the graph has 9 vertices and is represented by the adjacency matrix g.graph. 
# The dijkstra method is called with the source vertex 0. The output of the program is the shortest 

# distance from the source vertex to all other vertices in the graph

# Define a Graph class
class Graph():

    # Constructor to initialize the graph
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices in the graph
        # Create a 2D array (matrix) for the adjacency matrix representation of the graph
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        # initializes self.graph as a square matrix with dimensions vertices x vertices, filled with zeros.


 
    # Function to print the solution
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
            # print the node and its distance

    # Function to find the vertex with the minimum distance value, from those not yet 
    # included in the shortest path tree
    def minDistance(self, dist, sptSet):
        min = 1e7  # Initialize the minimum distance to a very high value (infinity)

        # Loop to find the nearest vertex not yet included in the shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]  # Update the minimum distance
                min_index = v  # Update the index of the vertex with the minimum distance

        return min_index

    def dijkstra(self, src):
            # Initialize a list to hold the shortest distance from the source to each vertex.
        # Initially, set all distances to a very large number (1e7, which acts like infinity)
        dist = [1e7] * self.V  

        # Set the distance from the source to itself to 0, as it is the starting point.
        dist[src] = 0

        # Create a set (sptSet) to track vertices included in the shortest path tree (SPT).
        # Initially, no vertices are included in the SPT, so all values are False.
        sptSet = [False] * self.V

        # Loop over all vertices
        for cout in range(self.V):
            # Find the vertex with the minimum distance from the set of vertices
            # that haven't been included in the SPT yet.
            u = self.minDistance(dist, sptSet)

            # Add the vertex with the minimum distance to the SPT.
            sptSet[u] = True

            # Update the distance of all adjacent vertices of the picked vertex.
            for v in range(self.V):
                # Check if there's an edge between u and v (graph[u][v] > 0),
                # the vertex v is not in the SPT yet (sptSet[v] == False),
                # and the path through u to v offers a shorter distance than the current distance value for v.
                # If all conditions are met, update the distance for v.
                if (
                    self.graph[u][v] > 0 
                    and not sptSet[v] 
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        # After calculating the shortest paths, call the function to print the solution.
        self.printSolution(dist)


# Example to demonstrate the implementation:

# Create a graph with 9 vertices
g = Graph(9)

# Manually set the adjacency matrix of the graph
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

# Call Dijkstra's algorithm with the source vertex as 0
g.dijkstra(3)
