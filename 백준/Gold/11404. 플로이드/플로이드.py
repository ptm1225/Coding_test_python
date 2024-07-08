import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    arr[i][i] = 0

for _ in range(m):
    i, j, w = map(int, input().split())
    i, j = i-1, j-1
    arr[i][j] = min(arr[i][j], w)

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(n):
    for j in range(n):
        print(arr[i][j] if arr[i][j] != float('inf') else 0, end=' ')
    print()