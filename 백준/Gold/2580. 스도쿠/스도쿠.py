arr = [list(map(int, input().split())) for _ in range(9)]
d = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            d.append((i, j))
cnt = len(d)

def f(idx):
    if idx == cnt:
        for i in range(9):
            print(*arr[i])
        exit()

    x, y = d[idx][0], d[idx][1]
    
    for v in range(1, 10):
        if not (v in arr[x] or v in list(arr[z][y] for z in range(9)) or v in list(arr[n][m] for n in range((x//3)*3, (x//3+1)*3) for m in range((y//3)*3, (y//3+1)*3))):
            arr[x][y] = v
            f(idx+1)
            arr[x][y] = 0

f(0)
