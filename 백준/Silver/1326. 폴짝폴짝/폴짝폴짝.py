from collections import deque
n = int(input())
bridge = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

queue = deque([a])
visited = [-1] * (n+1)
visited[a] = 0

while queue:
    idx = queue.popleft()
    for i in range(idx + bridge[idx], n+1, bridge[idx]):
        if visited[i] == -1:
            visited[i] = visited[idx] + 1
            queue.append(i)
    for i in range(idx - bridge[idx], 0, -bridge[idx]):
        if visited[i] == -1:
            visited[i] = visited[idx] + 1
            queue.append(i)

print(visited[b])