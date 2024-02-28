n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

def dfs(s, i, j, arr):
    if not (i < 0 or j < 0 or i > len(arr)-1 or j > len(arr[0])-1 or arr[i][j] == 'x') and arr[i][j] == s:
        arr[i][j] = 'x'
        if s == '-':
            dfs(s, i, j-1, arr)
            dfs(s, i, j+1, arr)
        elif s == '|':
            dfs(s, i+1, j, arr)
            dfs(s, i-1, j, arr)

count = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != 'x':
            dfs(arr[i][j], i, j, arr)
            count += 1

print(count)