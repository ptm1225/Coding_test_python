import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().rstrip()
    K = int(input())
    d = defaultdict(list)

    one = 10 ** 6
    two = -1
    for i, s in enumerate(W):
        d[s].append(i)
        if len(d[s]) >= K:
            one = min(one, d[s][-1] - d[s][-K] + 1)
            two = max(two, d[s][-1] - d[s][-K] + 1)
    if one == 10 ** 6 or two == -1:
        print(-1)
    else:
        print(one, two)