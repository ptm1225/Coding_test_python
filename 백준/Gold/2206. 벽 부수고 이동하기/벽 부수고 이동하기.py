import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append([int(x) for x in input().rstrip()])

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(i, j, tx, ty):
    q = deque()
    q.append((i, j, 1))
    cnt = 1
    while q:
        for _ in range(len(q)):
            x, y, z = q.popleft()
            if x == tx and y == ty:
                return cnt
            for a, b in d:
                if 0 <= x+a < n and 0 <= y+b < m and visited[x+a][y+b] != 2:
                    if visited[x+a][y+b] == 0:
                        q.append((x+a, y+b, z))
                        visited[x+a][y+b] = 2
                    elif visited[x+a][y+b] == 1 and z == 1:
                        q.append((x+a, y+b, 0))
                        visited[x+a][y+b] = 2
        cnt += 1
    return 0

visited = deepcopy(arr)
a = bfs(0, 0, n-1, m-1)
visited = deepcopy(arr)
b = bfs(n-1, m-1, 0, 0)

if a and b:
    print(min(a, b))
elif a and not b:
    print(a)
elif not a and b:
    print(b)
else:
    print(-1)