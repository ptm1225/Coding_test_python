from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    arr = []
    
    dx = [0, 0, 1, -1] # 동, 서, 남, 북
    dy = [1, -1, 0, 0]
    
    q.append((0, 0, 1))
    
    while q:
        current = q.popleft()
        x, y, count = current
        
        if x < 0 or y < 0 or x > n-1 or y > m-1 or visited[x][y] or maps[x][y] == 0:
            continue
        else:
            visited[x][y] = True
            maps[x][y] = count
            
            if x == n-1 and y == m-1:
                arr.append(maps[x][y])
                break
            
            count += 1
            for i in range(4):
                nx, ny = x, y
                nx += dx[i]
                ny += dy[i]
                q.append((nx, ny, count))
    
    if arr:
        return min(arr)
    else:
        return -1