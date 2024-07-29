import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(x, cnt):
    if cnt == 4:
        print(1)
        exit(0)

    for v in adj[x]:
        if not visited[v]:
            visited[v] = 1
            dfs(v, cnt+1)
            visited[v] = 0

visited = [0] * N
for i in range(N):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0
print(0)