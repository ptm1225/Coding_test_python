n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input().split())
    
result = [[-1]*m for _ in range(n)]

x, y = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '2':
            x, y = i, j
            break

queue = [(x, y)]
count = 0
while queue:
    for _ in range(len(queue)):
        i, j = queue.pop(0)
        if i < 0 or j < 0 or i > n-1 or j > m-1 or arr[i][j] == '0':
            continue
        if result[i][j] == -1:
            result[i][j] = count
            queue.append((i-1, j))
            queue.append((i+1, j))
            queue.append((i, j+1))
            queue.append((i, j-1))
    count += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            print(0, end=' ')
        else:
            print(result[i][j], end=' ')
    print()