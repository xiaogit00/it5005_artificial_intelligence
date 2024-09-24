
### BFS
BFS is good, in that it is pretty simple to implement. However, one major downside is its memory requirement. Its space complexity is a function of its branching factor and depth. Specifically, it is an exponential function of b^d. 

Assuming a branching factor of 10, and at a processing speed of 1M node/sec and 1kb/node, a search of depth 10 will take 3 hours, but would require 10 TB of memory. 

Therefore, memory requirements are a bigger problem for BFS than execution time.  At depth 14, even with infinite memory, the search will take 3.5 years. 

### An insight we can draw now is this: exponential-complexity search problems can't be solved by uninformed search for any but the smallest instances. 


### On why the time complexity of Djikstra is b^(1 + ⌊C*/ǫ⌋)

The complexity O(b^(1 + ⌊C*/ǫ⌋)) essentially says that:

The number of nodes expanded grows exponentially with the number of cost layers (⌊C*/ǫ⌋), and
For each layer, the algorithm can explore up to b neighbors (branching factor).
This is a more nuanced way to express the complexity of Dijkstra's algorithm compared to the usual O((n + m) log n) analysis, because it takes into account how the edge costs affect the progression of the search.

