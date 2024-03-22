from math import inf as INF
n, m = map(int, input().split())
node = [INF] * (n+1)
edges = []

for _ in range(m):
    edges.append(list(map(int, input().split())))

node[1] = 0
for _ in range(n-1):
    for e in edges:
        u, v, w = e
        if node[v] > node[u] + w:
            node[v] = node[u] + w

for e in edges:
    u, v, w = e
    if node[v] > node[u] + w:
        print(-1)
        break
else:
    for v in range(2, n+1):
        print(-1 if node[v] == INF else node[v])