n, m = map(int, input().split())
arr = list(range(1, n+1))
for _ in range(m):
    i, j = map(int, input().split())
    for x in range((j-i+1)//2):
        arr[i+x-1], arr[j-x-1] = arr[j-x-1], arr[i+x-1]
print(*arr)