def dfs(i, j, arr):
    if i < 0 or j < 0 or i > len(arr[0])-1 or j > len(arr)-1 or arr[j][i] == 0 or arr[j][i] == 2:
        pass
    elif arr[j][i] == 1:
        arr[j][i] += 1
        dfs(i-1, j, arr)
        dfs(i+1, j, arr)
        dfs(i, j-1, arr)
        dfs(i, j+1, arr)

t = int(input())
result = []
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(int(k)):
        x, y = map(int, input().split())
        arr[y][x] = 1
        
    count = 0
    for i in range(m):
        for j in range(n):
            if arr[j][i] == 1:
                dfs(i, j, arr)
                count += 1
    result.append(count)

for r in result:
    print(r)