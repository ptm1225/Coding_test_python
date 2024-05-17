from math import inf
import heapq
n, m, x = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

result = [0] * (n+1)

for s in range(1, n+1):
    node = [inf] * (n+1)
    node[s] = 0
    
    q = []
    heapq.heappush(q, (0, s))
    
    while q:
        cost, u = heapq.heappop(q)
        for v, w in adj[u]:
            if node[u] + w < node[v]:
                node[v] = node[u] + w
                heapq.heappush(q, (node[v], v))
    if s != x:
        result[s] += node[x]
    else:
        for i, v in enumerate(node):
            if i != x:
                result[i] += v
result.remove(inf)
print(max(result))