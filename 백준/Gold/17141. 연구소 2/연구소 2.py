from copy import deepcopy
from itertools import combinations
from collections import deque
n, m = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
if sum(t[i].count(1) for i in range(n)) == n**2:
    print(0)
    exit()
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

virus = []
for i in range(n):
    for j in range(n):
        if t[i][j] == 2:
            virus.append((i, j))

def f(v):
    arr = deepcopy(t)
    q = deque()
    
    for x, y in v:
        arr[x][y] = 3
        q.append((x, y))
    
    cnt = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for x, y in d:
                if 0 <= i+x < n and 0 <= j+y < n and (arr[i+x][j+y] == 0 or arr[i+x][j+y] == 2):
                    arr[i+x][j+y] = 3
                    q.append((i+x, j+y))
        cnt += 1
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0 or arr[i][j] == 2:
                return float('inf')
    return cnt-1

result = float('inf')
for v in combinations(virus, m):
    c = f(v)
    result = min(result, c)
print(-1 if result == float('inf') else result)