n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(int(input())):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

queue = [1]
visited = [False]*(n+1)
while queue:
    v = queue.pop(0)
    if not visited[v]:
        visited[v] = True
        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
print(sum(visited)-1)