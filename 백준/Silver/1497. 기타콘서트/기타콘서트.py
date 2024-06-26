import sys
from itertools import combinations
input = sys.stdin.readline


N, M = map(int, input().split())
d = [[] for _ in range(N)]
for i in range(N):
    name, b = input().split()
    for j in b:
        d[i].append(1 if j == 'Y' else 0)

result = [0] * (N+1)

for c in range(1, N+1):
    for x in combinations(d, c):
        s = [0] * M
        for l in x:
            for i, v in enumerate(l):
                s[i] += v
        result[c] = max(result[c], M-s.count(0))
ans = result.index(max(result))
print(ans if ans != 0 else -1)