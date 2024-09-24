import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.h = {}  # Heuristic values

    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))

    def set_heuristic(self, node, value):
        self.h[node] = value

def best_first_search(graph, start, goal):
    # Priority queue to store (heuristic, current_node, path)
    priority_queue = []
    heapq.heappush(priority_queue, (graph.h[start], start, [start]))
    
    visited = set()
    
    while priority_queue:
        _, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return path  # Return the path if we reach the goal
        
        if current_node not in visited:
            visited.add(current_node)

            for neighbor, cost in graph.edges.get(current_node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (graph.h[neighbor], neighbor, path + [neighbor]))

    return None  # Return None if no path is found

# Example usage:
graph = Graph()

# Add edges (from_node, to_node, cost)
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'D', 4)
graph.add_edge('B', 'E', 2)
graph.add_edge('C', 'F', 5)
graph.add_edge('E', 'G', 2)
graph.add_edge('F', 'G', 1)

# Set heuristic values for each node
graph.set_heuristic('A', 6)
graph.set_heuristic('B', 4)
graph.set_heuristic('C', 5)
graph.set_heuristic('D', 4)
graph.set_heuristic('E', 2)
graph.set_heuristic('F', 3)
graph.set_heuristic('G', 0)

# Perform Best First Search
start = 'A'
goal = 'G'
path = best_first_search(graph, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found.")
