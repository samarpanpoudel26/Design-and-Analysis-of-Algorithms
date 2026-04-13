import heapq

def dijkstra(n, adj, source):
    dist=[float("inf")]*n
    dist[source]=0
    min_heap=[(0,source)]
    while min_heap:
        current_dist,u=heapq.heappop(min_heap)
        print("current_dist,u:",current_dist,u)
        print("min_heap:",min_heap)
        print("dist:",dist[u])
        if current_dist>dist[u]:
            continue
        for v,weight in adj[u]:
            new_dist=current_dist+weight
            if new_dist<dist[v]:
                dist[v]=new_dist
                heapq.heappush(min_heap,(new_dist,v))
    return dist

# Example usage
if __name__ == "__main__":
    # Number of nodes
    n = 5

    # Graph adjacency list (directed or undirected)
    adj = {
        0: [(1, 2), (2, 4)],
        1: [(2, 1), (3, 7)],
        2: [(4, 3)],
        3: [(4, 1)],
        4: []
    }

    # Source node
    source = 0

    # Run Dijkstra's algorithm
    distances = dijkstra(n, adj, source)

    # Print shortest distances from source
    print("Shortest distances from source node", source)
    for i, d in enumerate(distances):
        print(f"{source} → {i} = {d}")