from collections import deque

def solution(n, edge):
    adj = [[] for _ in range(n+1)]
    for u, v in edge:
        adj[u].append(v)
        adj[v].append(u)
    q = deque([(1, 0)])
    visited = [0] * (n+1)
    visited[1] = True
    result = [0] * (n+1)
    while q:
        u, cnt = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                result[v] = cnt+1
                q.append((v, cnt+1))
    m = max(result)
    return result.count(m)