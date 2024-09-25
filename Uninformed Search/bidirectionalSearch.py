from collections import deque

def bidirectional_search(graph, start, goal):
    # Initialize frontiers (queues for BFS) for both searches
    front_start = deque([start])  # Search from start to goal
    front_goal = deque([goal])    # Search from goal to start
    
    # Visited nodes and their parents for path reconstruction
    visited_start = {start: None}
    visited_goal = {goal: None}

    while front_start and front_goal:
        # Expand the forward search from the start
        if front_start:
            node = front_start.popleft()
            if node in visited_goal:
                # Path found! Reconstruct and return the path
                return construct_path(visited_start, visited_goal, node)
            for neighbor in graph[node]:
                if neighbor not in visited_start:
                    visited_start[neighbor] = node
                    front_start.append(neighbor)

        # Expand the backward search from the goal
        if front_goal:
            node = front_goal.popleft()
            if node in visited_start:
                # Path found! Reconstruct and return the path
                return construct_path(visited_start, visited_goal, node)
            for neighbor in graph[node]:
                if neighbor not in visited_goal:
                    visited_goal[neighbor] = node
                    front_goal.append(neighbor)

    # If no path is found, return None
    return None

def construct_path(visited_start, visited_goal, meet_point):
    # Reconstruct path from start to meet_point
    path_start = []
    node = meet_point
    while node is not None:
        path_start.append(node)
        node = visited_start[node]
    path_start.reverse()

    # Reconstruct path from meet_point to goal
    path_goal = []
    node = visited_goal[meet_point]
    while node is not None:
        path_goal.append(node)
        node = visited_goal[node]

    # Concatenate the two halves of the path
    return path_start + path_goal

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

start_node = 'A'
goal_node = 'G'
path = bidirectional_search(graph, start_node, goal_node)
print("Path found:", path)
