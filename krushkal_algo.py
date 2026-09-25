class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: source destination weight")

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# Sort edges according to weight
edges.sort()

ds = DisjointSet(n)

mst = []
total_weight = 0

for weight, u, v in edges:
    if ds.union(u, v):
        mst.append((u, v, weight))
        total_weight += weight

print("\nEdges in Minimum Spanning Tree:")

for u, v, weight in mst:
    print(u, "--", v, "=", weight)

print("Total weight:", total_weight)
