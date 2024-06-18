import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, r = map(int, input().split())
visited = [0] * (n+1)
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in adj:
    i.sort()

cnt = 0
def dfs(i):
    global cnt
    cnt += 1
    visited[i] = cnt
    for v in adj[i]:
        if not visited[v]:
            dfs(v)
dfs(r)

for i in range(1, n+1):
    print(visited[i])