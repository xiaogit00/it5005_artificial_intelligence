'''
The general idea of DLS is that it's very similar to DFS, but with a limit.

IDS is just DLS repeatedly. 
'''


def depthLimitSearch(s, limit, goal):
    frontier = []
    result = "Failure"
    while frontier:
        v = frontier.pop()
        if v == goal:
            return v
        if v.depth > limit:
            result = "Cutoff"
        else:
            if isCycle(v): continue # because it doesn't use reached, need to check
            for u in v.children:
                frontier.append(u)
    return result

def iterativeDeepeningSearch(s):
    for depth in range(0, 100000):
        result = depthLimitSearch(s, depth)
        if result != "Cutoff": return result #in this case, return is exiting
        # result can be node, failure, or cutoff. for node and failure,
        # we are returning result, exiting the code. 
        # So in positive case, we return node, or failure. If cutoff, 
        # we increment the depth and continue. 