from queue import PriorityQueue

# Define the Romania map (graph) as an adjacency list
romania_map = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90)],
    'Giurgiu': [('Bucharest', 90)]
}

# Define the heuristic (straight-line distance to Bucharest)
h = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Fagaras': 178,
    'Rimnicu Vilcea': 193, 'Pitesti': 98, 'Timisoara': 329, 'Lugoj': 244,
    'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160, 'Bucharest': 0, 'Giurgiu': 77
}

# Greedy Best-First Search Algorithm
def greedy_best_first_search(start, goal):
    # PriorityQueue stores (heuristic, city)
    frontier = PriorityQueue()
    frontier.put((h[start], start))
    explored = set()
    path = []
    
    while not frontier.empty():
        # Get the city with the lowest heuristic value
        _, current_city = frontier.get()
        path.append(current_city)
        
        # If we reach the goal, return the path
        if current_city == goal:
            return path
        
        # Mark the city as explored
        explored.add(current_city)
        
        # Expand the city and add its neighbors to the frontier
        for neighbor, _ in romania_map[current_city]:
            if neighbor not in explored:
                frontier.put((h[neighbor], neighbor))
    
    return None  # If no path is found

# Find the path from Arad to Bucharest using Greedy Best-First Search
path = greedy_best_first_search('Arad', 'Bucharest')
print("Path from Arad to Bucharest:", path)
