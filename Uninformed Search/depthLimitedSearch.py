class Node:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

def depth_limited_search(start_state, goal_state, successors, limit):
    """
    Performs depth-limited search (DLS) to find a goal state.
    
    :param start_state: Initial state to start the search.
    :param goal_state: The target state we are trying to reach.
    :param successors: A function that returns a list of (action, next_state) pairs.
    :param limit: Depth limit for the search.
    
    :return: A solution path if the goal is found, otherwise None.
    """
    def recursive_dls(node, limit):
        if node.state == goal_state:
            return solution(node)
        elif limit == 0:
            return None  # Reached the depth limit
        else:
            cutoff_occurred = False
            for action, child_state in successors(node.state):
                child_node = Node(child_state, node, action, node.depth + 1)
                result = recursive_dls(child_node, limit - 1)
                if result is not None:
                    return result
                cutoff_occurred = True
            return None if cutoff_occurred else 'cutoff'
    
    return recursive_dls(Node(start_state), limit)

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
limit = 3

result = depth_limited_search(start, goal, example_successors, limit)

if result is not None:
    print("Solution found:", result)
else:
    print("No solution found within the depth limit.")
