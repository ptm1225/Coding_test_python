from collections import defaultdict

N = int(input())
d = defaultdict(int)

for _ in range(N):
    for i, v in enumerate(input()[::-1]):
        d[v] += 10 ** i

d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

w = 9
result = 0

for k, v in d.items():
    if v:
        result += w*v
        w -= 1
print(result)