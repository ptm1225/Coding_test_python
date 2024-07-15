import sys
from collections import deque
input = sys.stdin.readline

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input().rstrip())

def bfs(i, j):
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt = 0
    
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for x, y in d:
                nx = x+i
                ny = y+j
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 'L':
                    visited[nx][ny] = 1
                    q.append((nx, ny))
        cnt += 1
    return cnt

result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            result = max(result, bfs(i, j)-1)
print(result)