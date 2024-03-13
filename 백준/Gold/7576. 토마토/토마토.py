from collections import deque
m, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

queue = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j))
            arr[i][j] = 0

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

count = -2
while queue:
    for _ in range(len(queue)):
        i, j = queue.popleft()
        if 0 <= i < n and 0 <= j < m and arr[i][j] == 0:
            arr[i][j] = 1
            for x in range(4):
                ni = i+di[x]
                nj = j+dj[x]
                queue.append((ni, nj))
    count += 1

is_error = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            is_error = True
            break
if is_error:
    print(-1)
else:
    print(count)