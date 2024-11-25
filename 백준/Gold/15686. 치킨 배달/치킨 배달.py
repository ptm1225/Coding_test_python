from itertools import combinations
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

result = float('inf')
for z in combinations(chicken, m):
    total = 0
    for i, j in house:
        total += min(abs(x-i)+abs(y-j) for x, y in z)
    result = min(result, total)
print(result)