from collections import deque
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for x, y in d:
            if 0 <= i+x < N and 0 <= j+y < M and arr[i+x][j+y] != 0 and not visited[i+x][j+y]:
                visited[i+x][j+y] = 1
                q.append((i+x, j+y))

cnt = 0
while True:
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                break
        else:
            continue
        break
    else:
        print(0)
        exit(0)

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] != 0:
                print(cnt)
                exit(0)

    z = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                z.append((i, j, sum(1 for x, y in d if arr[i+x][j+y] == 0)))

    for i, j, w in z:
        arr[i][j] -= w
        if arr[i][j] < 0:
            arr[i][j] = 0
    
    cnt += 1