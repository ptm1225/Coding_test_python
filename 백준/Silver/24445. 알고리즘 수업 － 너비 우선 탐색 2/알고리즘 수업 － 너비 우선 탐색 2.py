import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for x in adj:
    x.sort(reverse=True)

visited = [0] * (n+1)
cnt = 1
q = deque()
q.append(r)
visited[r] = cnt
while q:
    u = q.popleft()
    for v in adj[u]:
        if not visited[v]:
            cnt += 1
            visited[v] = cnt
            q.append(v)
for v in visited[1:]:
    print(v)