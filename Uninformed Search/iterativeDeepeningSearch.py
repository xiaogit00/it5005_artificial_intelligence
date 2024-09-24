class Node:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

def iterative_deepening_search(start_state, goal_state, successors):
    """
    Performs iterative deepening search (IDS) to find a goal state.
    
    :param start_state: Initial state to start the search.
    :param goal_state: The target state we are trying to reach.
    :param successors: A function that returns a list of (action, next_state) pairs.
    
    :return: A solution path if the goal is found, otherwise None.
    """
    def depth_limited_search(node, limit):
        if node.state == goal_state:
            return solution(node)
        elif limit == 0:
            return None  # Reached the depth limit
        else:
            cutoff_occurred = False
            for action, child_state in successors(node.state):
                child_node = Node(child_state, node, action, node.depth + 1)
                result = depth_limited_search(child_node, limit - 1)
                if result is not None:
                    return result
            return None
    
    depth = 0
    while True:
        print(f"Searching at depth: {depth}")
        result = depth_limited_search(Node(start_state), depth)
        if result is not None:
            return result
        depth += 1  # Increase depth limit

def solution(node):
    """
    Returns the path from the start state to the goal state.
    
    :param node: The goal node.
    :return: List of actions leading to the goal.
    """
    actions = []
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()
    return actions

# Example usage
def example_successors(state):
    # Example successor function for a graph-like state space
    graph = {
        'A': [('move to B', 'B'), ('move to C', 'C')],
        'B': [('move to D', 'D'), ('move to E', 'E')],
        'C': [('move to F', 'F')],
        'D': [],
        'E': [('move to G', 'G')],
        'F': [],
        'G': []
    }
    return graph.get(state, [])

start = 'A'
goal = 'G'

result = iterative_deepening_search(start, goal, example_successors)

if result is not None:
    print("Solution found:", result)
else:
    print("No solution found.")
