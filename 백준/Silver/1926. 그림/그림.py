from collections import deque
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 0
    while q:
        i, j = q.popleft()
        if 0<=i<n and 0<=j<m and arr[i][j] == 1:
            arr[i][j] = 0
            cnt += 1
            for _ in range(4):
                q.append((di[_]+i, dj[_]+j))
    return cnt

result = 0
t = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            t += 1
            c = bfs(i, j)
            result = max(result, c)
print(t)
print(result)