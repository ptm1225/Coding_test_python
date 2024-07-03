from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    arr = [[0]*102 for _ in range(102)]
    for r in rectangle:
        r = list(map(lambda x:x*2, r))
        for i in [r[0], r[2]]:
            for j in range(r[1], r[3]+1):
                if arr[i][j] == 0:
                    arr[i][j] = 1
        for i in [r[1], r[3]]:
            for j in range(r[0], r[2]+1):
                if arr[j][i] == 0:
                    arr[j][i] = 1
        for i in range(r[0]+1, r[2]):
            for j in range(r[1]+1, r[3]):
                arr[i][j] = 2
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    characterX, characterY, itemX, itemY = map(lambda x:2*x, [characterX, characterY, itemX, itemY])
    def bfs():
        q = deque([(characterX, characterY)])
        arr[characterX][characterY] = 2
        cnt = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if x == itemX and y == itemY:
                    return cnt
                for a, b in d:
                    nx, ny = x+a, y+b
                    if 0 <= nx < 102 and 0 <= ny < 102 and arr[nx][ny] == 1:
                        q.append((nx, ny))
                        arr[nx][ny] = 2
            cnt += 1
        return -1
    return bfs() // 2
    