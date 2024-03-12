from collections import deque
m, n, h = map(int, input().split())
arr = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        arr[i].append(list(map(int, input().split())))

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append((i,j,k))
                arr[i][j][k] = 0

di = [-1,1,0,0,0,0]
dj = [0,0,1,-1,0,0]
dk = [0,0,0,0,1,-1]

count = -2
while queue:
    for _ in range(len(queue)):
        i,j,k = queue.popleft()
        if 0 <= i < h and 0 <= j < n and 0 <= k < m and arr[i][j][k] == 0:
            arr[i][j][k] = 1
            for idx in range(6):
                ni = i + di[idx]
                nj = j + dj[idx]
                nk = k + dk[idx]
                queue.append((ni,nj,nk))
    count += 1

z = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                z = False
                break

if z:
    print(count)
else:
    print(-1)