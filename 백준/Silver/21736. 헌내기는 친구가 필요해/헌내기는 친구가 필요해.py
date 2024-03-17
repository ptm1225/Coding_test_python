from collections import deque
n, m = map(int, input().split())
arr = []
count = 0
for _ in range(n):
    arr.append(list(input()))

def bfs(i, j):
    q = deque([(i, j)])
    while q:
        i, j = q.popleft()
        if 0 <= i < n and 0 <= j < m and arr[i][j] != 'X':
            if arr[i][j] == 'P':
                global count
                count += 1
            arr[i][j] = 'X'
            q.append((i+1, j))
            q.append((i-1, j))
            q.append((i, j+1))
            q.append((i, j-1))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            bfs(i, j)
            break
print(count if count else 'TT')