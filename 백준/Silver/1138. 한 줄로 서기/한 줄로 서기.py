n = int(input())
inp = map(int, input().split())
arr = [100] * n
visited = [False] * n

for i, v in enumerate(inp):
    i = i+1
    x = 0
    while v:
        if arr[x] > i:
            v -= 1
        x += 1
    for j in range(x, n):
        if not visited[j]:
            arr[j] = i
            visited[j] = True
            break

for a in arr:
    print(a, end=' ')