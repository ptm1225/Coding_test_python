m, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())
visited = [[False] * m for _ in range(n)]
d = {'W':0, 'B':0}
r = {'W':0, 'B':0}
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(i, j, color):
    visited[i][j] = True
    d[color] += 1
    for x in range(4):
        a = di[x] + i
        b = dj[x] + j
        if 0 <= a < n and 0 <= b < m and not visited[a][b] and arr[a][b] == color:
            dfs(a, b, color)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            color = arr[i][j]
            dfs(i, j, color)
            r[color] += d[color] ** 2
            d[color] = 0
print(*r.values())