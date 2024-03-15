from collections import deque
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(x, y, color):
    q = deque([(x, y)])
    while q:
        i, j = q.popleft()
        if 0 <= i < n and 0 <= j < n and arr[i][j] == color and not visited[i][j]:
            visited[i][j] = True
            for k in range(4):
                q.append((i+di[k], j+dj[k]))

visited = [[False]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, arr[i][j])
            count += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited = [[False]*n for _ in range(n)]
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, arr[i][j])
            count2 += 1
print(count, count2)