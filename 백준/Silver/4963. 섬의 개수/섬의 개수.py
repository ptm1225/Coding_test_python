from collections import deque
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]

    def dfs(i, j):
        arr[i][j] = 0
        for x in range(8):
            di = i + dx[x]
            dj = j + dy[x]
            if 0 <= di < h and 0 <= dj < w and arr[di][dj] == 1:
                dfs(di, dj)
                
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)