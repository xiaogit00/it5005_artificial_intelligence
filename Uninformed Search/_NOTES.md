
### BFS
BFS is good, in that it is pretty simple to implement. However, one major downside is its memory requirement. Its space complexity is a function of its branching factor and depth. Specifically, it is an exponential function of b^d. 

Assuming a branching factor of 10, and at a processing speed of 1M node/sec and 1kb/node, a search of depth 10 will take 3 hours, but would require 10 TB of memory. 

Therefore, memory requirements are a bigger problem for BFS than execution time.  At depth 14, even with infinite memory, the search will take 3.5 years. 

#### An insight we can draw now is this: exponential-complexity search problems can't be solved by uninformed search for any but the smallest instances. 


### On why the time complexity of Djikstra is b^(1 + ⌊C*/ǫ⌋)

The complexity O(b^(1 + ⌊C*/ǫ⌋)) essentially says that:

The number of nodes expanded grows exponentially with the number of cost layers (⌊C*/ǫ⌋), and
For each layer, the algorithm can explore up to b neighbors (branching factor).
This is a more nuanced way to express the complexity of Dijkstra's algorithm compared to the usual O((n + m) log n) analysis, because it takes into account how the edge costs affect the progression of the search.

### Properties of DFS
Depth first search is not cost optimal (whether it finds a solution with the lowest path cost of all solutions), because it returns the first solution it finds, even if it is not the cheapest. 

**However**, it has far smaller needs for memory. We don't keep a reached table - and the frontier is very small. Norvig puts it very well: "think of the frontier of a BFS as the surface of an ever-expanding sphere, while the frontier in DFS is just a radius of a sphere". 

In addition, DFS has the following properties: 
- for **finite** state spaces that are trees, DFS is efficient and complete. 
- for **acyclic** (DAG) spaces, it might end up expanding same state many times via different paths (cos don't store reached), but will epxlore entire space (complete)
- in **cyclic** state spaces, it can get stuck in infinite loops; therefore some implementation checks for cycles
- In **infinite** state spaces, DFS is not systematic - can get stuck going down infinite path. 

#### Time complexity of DFS
In tree shaped state space, DFS takes time proportional to number of states, and has memory complexity of O(bm) where *b* is the branching factor and *m* is the max depth of the tree. Because of its low memory requirements, DFS used as basic workhorse in many areas of AI. 

#### Variant of DFS with even less memory requirements: Backtracking search
How is it implemented?
- only one successor generated at a time 
- each partially expanded node rmbs which successor to generate next
- successors generated by modifying current state directly rather than allocate memory for brand-new state
- reduces memory requirements to just one state description and path of O(m) actions, better than O(bm)
- alao have options of maintaining a set data structure for states allowing us to check for cyclic path in O(1) 


### Time complexity of IDS
- The most bottom nodes are generated once, 2nd bottom is generated twice, etc. 
- Therefore, total number of nodes generated = d(b) + (d-1)b^2 + (d-2)b^3 ... + b^d. The top generated d times. 
- This gives time complexity of b^d. 
- Similar to BFS
- Comparing example: b=10, d=5
    - For IDS: 123,450
    - For BFS: 111110

Each iteration of IDS generates a new level, but BFS does this by storing all nodes in memory, while iterative deepening does it by repeating the previous levels, saving memory at the cost of time. 
**The states at top of search tree are regenerated at every iteration!**
**However** a key observation to counter this is that for many state spaces, most of the nodes are at bottom level, so it doesn't matter much that upper levels are repeated. 

#### When do we use IDS? 
It is the preferred uninformed search method when search state space is larger than can fit in memory and depth of the solution is not known. 

### The idea of search contours
- It allows you to visualize how a search 'expands' outwards. 
- For djikstra, the contours will be 'circular' around the start state. 
- For A* search with a good heuristic, the g+h bands will stretch toward a goal state. 