n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    s = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            s += arr[a][b]
    print(s)