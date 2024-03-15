from collections import deque
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

q = deque()
result = []
for i in range(1, n+1):
    q.append(i)
    visited = [-1] * (n+1)
    cnt = 0
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            if visited[v] == -1:
                visited[v] = cnt
                for i in arr[v]:
                    q.append(i)
        cnt += 1
    result.append(sum(visited)+1)

print(result.index(min(result)) + 1)