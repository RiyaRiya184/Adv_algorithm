INF = float('inf')

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: source destination weight")

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

source = int(input("Enter source vertex: "))

distance = [INF] * n
distance[source] = 0

# Relax all edges n-1 times
for _ in range(n - 1):
    updated = False

    for u, v, w in edges:
        if distance[u] != INF and distance[u] + w < distance[v]:
            distance[v] = distance[u] + w
            updated = True

    if not updated:
        break

# Check for negative weight cycle
negative_cycle = False

for u, v, w in edges:
    if distance[u] != INF and distance[u] + w < distance[v]:
        negative_cycle = True
        break

if negative_cycle:
    print("Graph contains a negative weight cycle.")
else:
    print("\nShortest distances from source", source)

    for i in range(n):
        if distance[i] == INF:
            print(i, ": INF")
        else:
            print(i, ":", distance[i])
