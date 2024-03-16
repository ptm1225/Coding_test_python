n, m = map(int, input().split())
arr = [0] * n
for _ in range(m):
    i, j, num = map(int, input().split())
    for x in range(i-1, j):
        arr[x] = num
print(*arr)