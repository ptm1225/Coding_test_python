from itertools import combinations as c
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
result = []

for a in arr:
    result.append(max(sum(x)%10 for x in c(a, 3)))

m = max(result)
r = []
for i, v in enumerate(result):
    if v == m:
        r.append(i+1)
print(max(r))