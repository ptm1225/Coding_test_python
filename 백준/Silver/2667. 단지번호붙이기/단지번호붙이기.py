from collections import deque
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

visited = [[False]*n for _ in range(n)]

def bfs(i, j):
    q = deque([(i, j)])
    cnt = 0
    while q:
        i, j = q.popleft()
        if 0 <= i < n and 0 <= j < n and arr[i][j] and not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            result.append(bfs(i, j))

print(len(result))
for r in sorted(result):
    print(r)