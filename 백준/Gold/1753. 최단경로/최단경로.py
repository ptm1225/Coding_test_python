from math import inf
V, E = map(int, input().split())
K = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

node = [inf] * (V+1)
node[K] = 0
i = 0
q = list(range(1, V+1))

while q:
    m = min(node[x] for x in q)
    for i in q:
        if node[i] == m:
            q.remove(i)
            break
    for v, w in adj[i]:
        if node[i] + w < node[v]:
            node[v] = node[i] + w
for i in range(1, V+1):
    print(node[i] if node[i] != inf else 'INF')