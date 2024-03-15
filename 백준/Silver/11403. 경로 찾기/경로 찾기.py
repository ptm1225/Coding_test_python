from collections import deque
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def bfs(s):
    q = deque([s])
    result = [0] * n
    while q:
        u = q.popleft()
        for i in range(n):
            if arr[u][i] == 1 and result[i] == 0:
                result[i] = 1
                q.append(i)
    return result

for i in range(n):
    print(*bfs(i))