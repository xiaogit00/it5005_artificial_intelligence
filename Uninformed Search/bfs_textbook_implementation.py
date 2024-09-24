from collections import deque

goal = ""

def bfs(s, goal):
    if s == goal: return s
    frontier = deque([s])
    reached = set(s.value)
    while frontier:
        u = frontier.popleft()
        for v in u.children:
            if v == goal: return v
            if v not in reached:
                reached.add(v)
                frontier.append(v)
    return False

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"Node({self.value})"

    def __eq__(self, other):
        return self.value == other.value
    
    def __hash__(self):
        # Hash the node based on its value
        return hash(self.value)
    
'''
Creating Test cases
'''
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')

A.add_child(B)
A.add_child(C)
B.add_child(D)
B.add_child(E)
C.add_child(F)
C.add_child(G)

result = bfs(A, G)
print(result)