import heapq
from math import inf

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

start, end = map(int, input().split())
node = [inf] * (n+1)
node[start] = 0
visited = [False] * (n+1)

heap = []
heapq.heappush(heap, [0, start])
while heap:
    z, u = heapq.heappop(heap)
    if not visited[u]:
        visited[u] = True
        for v, w in adj[u]:
            if node[u] + w < node[v]:
                node[v] = node[u] + w
                heapq.heappush(heap, [node[v], v])
print(node[end])