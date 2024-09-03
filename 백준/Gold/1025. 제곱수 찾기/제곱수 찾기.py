n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]
result = -1

for i in range(n):
    for j in range(m):
        for diff_x in range(-n, n):
            for diff_y in range(-m, m):
                tmp = ''
                x, y = i, j
                if diff_x == 0 and diff_y == 0:
                    continue
                while 0 <= x < n and 0 <= y < m:
                    tmp += str(arr[x][y])
                    if int(int(tmp)**0.5) ** 2 == int(tmp):
                        result = max(result, int(tmp))
                    x += diff_x
                    y += diff_y

print(result)