import heapq  # Importing the heapq module for priority queue operations

def dijkstra(graph, start):
    # Initialize a priority queue to store nodes along with their tentative distances.
    # The queue will be ordered by the distance value (the first element of each tuple).
    priority_queue = [(0, start)]
    
    # Create a dictionary to store the tentative distances of all nodes.
    # Initialize all distances to infinity, since initially, all distances are unknown.
    distances = {node: float('infinity') for node in graph}
    # Set the distance to the start node to 0, as it is the starting point.
    
    distances[start] = 0
    
    # Continue the loop until the priority queue is empty.
    while priority_queue:
        # Pop the node with the smallest tentative distance from the priority queue.
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the popped node's distance is greater than the recorded distance,
        # this means we have already found a shorter path to this node. Skip processing.
        if current_distance > distances[current_node]:
            continue

        # Iterate over the neighbors of the current node.
        for neighbor, weight in graph[current_node].items():
            # Calculate the distance to this neighbor via the current node.
            distance = current_distance + weight
            
            # If this path to the neighbor is shorter than any previously recorded path,
            # update the neighbor's tentative distance and add the neighbor to the priority queue.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Return the dictionary containing the shortest distances from the start node to each node.
    return distances

# Example usage of the function:

# Define a graph using a dictionary. The graph is represented as an adjacency list,
# where each node has a dictionary of its neighbors and the respective edge weights.
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Specify the start node for Dijkstra's algorithm.
start_node = 'A'

# Run the Dijkstra's algorithm on the graph starting from the specified node.
shortest_distances = dijkstra(graph, start_node)

# Print the shortest distances from the start node to each other node.
print(f"Shortest distances from {start_node}:")
for node, distance in shortest_distances.items():
    print(f"To {node}: {distance}")
