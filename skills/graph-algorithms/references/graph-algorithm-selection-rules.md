# Graph Algorithm Selection Rules

- Use BFS for unweighted shortest-path or minimum-hop reachability.
- Use DFS for cycle detection, connectivity exploration, and traversal-based classification.
- Use Dijkstra for non-negative weighted shortest paths.
- Use Bellman-Ford when negative edges exist and negative-cycle detection is required.
- Use topological sort when dependency ordering on DAGs is required.
- Use SCC algorithms (Kosaraju/Tarjan) when strongly connected components matter.
- Use A* when heuristic-guided pathfinding can reduce search cost with admissible heuristics.
- Use max-flow/min-cut algorithms when capacity-constrained flow optimization is required.
