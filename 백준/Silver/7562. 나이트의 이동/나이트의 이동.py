import sys
from collections import deque
input = sys.stdin.readline

d = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[False] * l for _ in range(l)]
    cnt = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == mx and y == my:
                return cnt
            for a, b in d:
                if 0 <= x+a < l and 0 <= y+b < l and not visited[x+a][y+b]:
                    q.append((x+a, y+b))
                    visited[x+a][y+b] = True
        cnt += 1

t = int(input())
for _ in range(t):
    l = int(input())
    cx, cy = map(int, input().split())
    mx, my = map(int, input().split())
    print(bfs(cx, cy))