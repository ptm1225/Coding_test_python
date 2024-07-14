import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

N, Q = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    adj[p].append((q, r))
    adj[q].append((p, r))

node = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    visited = [0] * (N+1)
    q = deque()
    q.append(i)
    visited[i] = 1

    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                node[i][v] = min(node[i][v], node[i][u], w)
                visited[v] = 1
                q.append(v)

for _ in range(Q):
    k, v = map(int, input().split())
    print(sum(1 for x in node[v] if x != INF and x >= k))