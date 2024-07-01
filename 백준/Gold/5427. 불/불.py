import sys
from collections import deque
input = sys.stdin.readline

def bfs(w, h, i, j, fire):
    visited1 = [[0]*h for _ in range(w)]
    visited2 = [[0]*h for _ in range(w)]
    
    f = deque()
    for x, y in fire:
        f.append((x, y))
        visited1[x][y] = True
    
    q = deque([(i, j)])
    visited2[i][j] = True
    cnt = 1
    while q:
        for _ in range(len(f)):
            x, y = f.popleft()
            for a, b in d:
                nx = x+a
                ny = y+b
                if 0 <= nx < w and 0 <= ny < h and arr[nx][ny] != '#' and not visited1[nx][ny]:
                    if arr[nx][ny] in '@.':
                        visited1[nx][ny] = 1
                        f.append((nx, ny))
        
        for _ in range(len(q)):
            x, y = q.popleft()
            for a, b in d:
                nx = x+a
                ny = y+b
                if not (0 <= nx < w and 0 <= ny < h) and arr[x][y] in '@.':
                    return cnt
                if 0 <= nx < w and 0 <= ny < h and arr[nx][ny] != '#' and not visited2[nx][ny]:
                    if arr[nx][ny] == '.' and not visited1[nx][ny]:
                        visited2[nx][ny] = 1
                        q.append((nx, ny))
        
        cnt += 1
    return 'IMPOSSIBLE'

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    arr = [input().rstrip() for _ in range(h)]
    fire = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire.append((i, j))
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                print(bfs(h, w, i, j, fire))
                break
