from itertools import combinations
n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(1, n+1):
    for a in combinations(arr, i):
        if sum(a) == s:
            count += 1
print(count)