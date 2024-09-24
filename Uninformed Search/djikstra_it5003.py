from heapq import heappop, heappush 
from math import inf

while True:
    n, m, q, s = map(int, input().split())
    if n == 0: break
    AL = [[] for _ in range(n)]
    d = [inf for _ in range(n)]
    d[0] = 0
    pq = []
    heappush(pq, (d[0], 0))

    for _ in range(m):
        u, v, w = map(int, input().split())
        AL[u].append((v, w)) 
    
    while pq:
        (w, u) = heappop(pq)
        if w > d[u]: continue
        for (v, wuv) in AL[u]: # for each neighbour v in u
            if d[u] + wuv < d[v]:
                d[v] = d[u] + wuv
                heappush(pq, (d[v], v))
    for _ in range(q):
        v = int(input())
        if d[v] < inf:
            print(d[v])
        else: 
            print('Impossible')
    print()

'''
###Notes on line 19: if w > d[u]: continue check

The line if w > d[u]: continue is a priority queue optimization in Dijkstra's algorithm. Here's what it does in context:

Explanation:
(w, u) = heappop(pq): This line removes the node u from the priority queue pq, where w is the tentative shortest distance (priority) to node u. The priority queue (pq) stores nodes in increasing order of their tentative distances.

if w > d[u]: This checks if the value w, which is the distance retrieved from the priority queue, is greater than the current known shortest distance d[u] to node u.

continue: If w > d[u] is true, it skips the rest of the current loop iteration and goes directly to the next one, effectively ignoring this entry.

Why is this check necessary?
In Dijkstra's algorithm, the same node can be added to the priority queue multiple times as its distance estimate is improved. For example, if you find a shorter path to node u, you update its distance and push it into the priority queue again.

However, the old (longer) distance for the same node u might still be in the priority queue, waiting to be processed. When you later pop this outdated distance, it is no longer useful because a shorter path has already been found.

Thus, if w > d[u] acts as a filter:

If the distance w you popped is greater than the current best-known distance d[u], it means this is an outdated entry and should be ignored.
If the condition holds, you continue to skip processing this entry and move to the next item in the priority queue.

Example:
Imagine the following scenario:

Initially, you find a path to node u with a distance of 10 and push (10, u) into the priority queue.
Later, you find a shorter path to node u with a distance of 5, so you push (5, u) into the priority queue.
When you pop from the priority queue, the entry (5, u) is processed first, and the shortest path to u is updated to 5.
But the old entry (10, u) is still in the queue, waiting to be processed.
When you eventually pop (10, u), it is no longer useful because the shortest distance to u is already known to be 5. The condition if w > d[u] prevents processing this outdated entry.
'''