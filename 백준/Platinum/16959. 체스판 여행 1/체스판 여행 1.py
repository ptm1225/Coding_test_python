from collections import deque

dy = [[1,-1,0,0],[1,-1,1,-1],[1,1,-1,-1,2,2,-2,-2]]
dx = [[0,0,1,-1],[1,1,-1,-1],[2,-2,2,-2,1,-1,1,-1]]

N = int(input())
arr = [[*map(int,input().split())] for i in range(N)]

def f():
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 1:
        return i, j

def bfs():
  visited = [[[[[0]*N*N for i in range(N)] for i in range(N)] for i in range(3)] for i in range(8)]
  q = deque([(p, *S, 1, 0, -1) for p in range(3)])
  while q:
    p, y, x, n, cnt, d = q.popleft()
    if visited[d][p][y][x][n]:
      continue
    visited[d][p][y][x][n] = 1
    if arr[y][x] == n+1:
      if n == N**2-1:
        return cnt
      q.appendleft((p, y, x, n+1, cnt, -1))
      continue
    for i in [1,2]:
      q.append(((p+i)%3, y, x, n, cnt+1, -1))
    for i in range(len(dy[p])):
      y1,x1 = y+dy[p][i],x+dx[p][i]
      if 0 <= y1 < N and 0 <= x1 < N:
        if p!=2 and i==d:
          q.appendleft((p, y1, x1, n, cnt, i))
        else:
          q.append((p, y1, x1, n, cnt+1, i))

S = f()
print(bfs())