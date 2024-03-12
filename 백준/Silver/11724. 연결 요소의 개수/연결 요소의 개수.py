import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().rstrip().split())
    arr[u].append(v)
    arr[v].append(u)

def dfs(i):
    visited[i] = True
    for x in arr[i]:
        if not visited[x]:
            dfs(x)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)