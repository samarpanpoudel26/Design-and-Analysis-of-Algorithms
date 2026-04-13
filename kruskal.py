class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        # Path Compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by Rank
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # cycle detected

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(n, edges):
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w

        # Stop early if MST is complete
        if len(mst) == n - 1:
            break

    return mst, total_weight


# Example usage
if __name__ == "__main__":
    n = 5
    edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9)
    ]

    mst, cost = kruskal(n, edges)

    print("Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")

    print("Total weight:", cost)