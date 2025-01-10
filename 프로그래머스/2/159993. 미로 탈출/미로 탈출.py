from collections import deque

def bfs(start_x, start_y, end_x, end_y, maps, n, m, target):
    visited = [[0]*m for _ in range(n)]
    visited[start_x][start_y] = 1
    q = deque()
    q.append((start_x, start_y, 0))
    
    while q:
        for _ in range(len(q)):
            x, y, cnt = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x+dx
                ny = y+dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X":
                    if maps[nx][ny] == target:
                        return cnt+1
                    else:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt+1))
    return -1
            
def solution(maps):
    q = deque()
    n = len(maps)
    m = len(maps[0])
    start_x, start_y = 0, 0
    lever_x, lever_y = 0, 0
    end_x, end_y = 0, 0
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start_x, start_y = i, j
            elif maps[i][j] == "L":
                lever_x, lever_y = i, j
            elif maps[i][j] == "E":
                end_x, end_y = i, j
    
    a = bfs(start_x, start_y, lever_x, lever_y, maps, n, m, "L")
    b = bfs(lever_x, lever_y, end_x, end_y, maps, n, m, "E")
    
    return a+b if a != -1 and b != -1 else -1