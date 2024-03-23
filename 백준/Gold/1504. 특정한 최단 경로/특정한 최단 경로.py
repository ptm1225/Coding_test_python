from math import inf as INF
n, e = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
v1, v2 = map(int, input().split())

def d(start):
    node = [INF] * (n+1)
    S = list(range(1, n+1))
    node[start] = 0
    while S:
        m = INF
        for i in S:
            m = min(m, node[i])
        for i in S:
            if node[i] == m:
                u = i
                break
        
        S.remove(u)
        
        for x in adj[u]:
            v, w = x[0], x[1]
            if node[v] > node[u] + w:
                node[v] = node[u] + w
    return node

one, two, thr = d(1), d(v1), d(v2)
answer = min(one[v1] + two[v2] + thr[n], one[v2] + thr[v1] + two[n])
if answer != INF:
    print(answer)
else:
    print(-1)