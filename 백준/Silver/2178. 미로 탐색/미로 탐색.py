n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())

visited = [[False]*m for _ in range(n)]

count = 1
queue = [[0, 0]]
end = False
while True:
    for _ in range(len(queue)):
        i, j = queue.pop(0)
        
        if i == n-1 and j == m-1:
            end = True
            break
        
        if i < 0 or j < 0 or i > n-1 or j > m-1 or arr[i][j] == '0':
            continue
        
        if not visited[i][j]:
            visited[i][j] = True
            queue.append([i-1, j])
            queue.append([i+1, j])
            queue.append([i, j+1])
            queue.append([i, j-1])
    if end:
        break
    count += 1
print(count)