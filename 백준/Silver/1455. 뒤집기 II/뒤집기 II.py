n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

cnt = 0

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if arr[i][j] == 1:
            cnt += 1
            
            for x in range(i + 1):
                for y in range(j + 1):
                    arr[x][y] = 1 - arr[x][y]

print(cnt)
