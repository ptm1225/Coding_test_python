import sys
from collections import deque
input = sys.stdin.readline

move = [0] + list(range(1, 101))
visited = [False] * 101

n, m = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    move[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    move[u] = v

def bfs():
    q = deque()
    q.append(1)
    visited[1] = True
    cnt = 0
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            if v == 100:
                return cnt
            for i in range(1, 7):
                if 1 <= v+i <= 100 and not visited[v+i]:
                    visited[v+i] = True
                    q.append(move[v+i])
        cnt += 1
print(bfs())