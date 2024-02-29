n, m, v = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


visited = [False] * (n+1)

def dfs(v, graph, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph, visited)

dfs(v, graph, visited)
print()

visited = [False] * (n+1)
queue = []

visited[v] = True
print(v, end=' ')
for i in graph[v]:
    queue.append(i)

while queue:
    v = queue.pop(0)
    if not visited[v]:
        visited[v] = True
        print(v, end=' ')
        for i in graph[v]:
            queue.append(i)