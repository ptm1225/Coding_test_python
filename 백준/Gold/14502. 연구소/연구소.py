import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y, z):
    tmp = deepcopy(arr)
    for i, j in [x, y, z]:
        tmp[i][j] = 1

    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i, j))
    while q:
        i, j = q.popleft()
        for x, y in d:
            if 0 <= i+x < n and 0 <= j+y < m and tmp[i+x][j+y] == 0:
                tmp[i+x][j+y] = 2
                q.append((i+x, j+y))
    return sum([x.count(0) for x in tmp])

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

l = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            l.append((i, j))

result = -1
for x, y, z in combinations(l, 3):
    result = max(result, bfs(x, y, z))
print(result)