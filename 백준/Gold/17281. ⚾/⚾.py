import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = 0
for x in permutations(range(1, 9), 8):
    x = list(x)[:3] + [0] + list(x)[3:]
    i = 0
    score = 0
    for y in arr:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if y[x[i]] == 0:
                out += 1
            elif y[x[i]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif y[x[i]] == 2:
                score += b2+b3
                b1, b2, b3 = 0, 1, b1
            elif y[x[i]] == 3:
                score += b1+b2+b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1+b2+b3+1
                b1, b2, b3 = 0, 0, 0
            i = (i+1) % 9
    result = max(result, score)

print(result)