import sys
from collections import deque
input = sys.stdin.readline

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

q = deque()
f = deque()
visited = [[0] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            arr[i][j] = '.'
            q.append((i, j))
            visited[i][j] = 1
        if arr[i][j] == 'F':
            f.append((i, j))

cnt = 0
while q:
    for _ in range(len(q)):
        i, j = q.popleft()
        for x, y in d:
            nx = i+x
            ny = j+y
            if not (0 <= nx < R and 0 <= ny < C) and arr[i][j] in '.J':
                print(cnt+1)
                exit(0)
            
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and arr[nx][ny] == '.':
                visited[nx][ny] = 1
                q.append((nx, ny))
    for _ in range(len(f)):
        i, j = f.popleft()
        for x, y in d:
            nx = i+x
            ny = j+y
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] in '.J':
                arr[nx][ny] = 'F'
                f.append((nx, ny))
    
    cnt += 1
print('IMPOSSIBLE')