from itertools import combinations

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))
cnt = 0
for a, b in combinations(arr, 2):
    for i, j in zip(a, b):
        if i != j:
            for x in range(len(a)):
                if a[x] == i:
                    a[x] = j
                elif a[x] == j:
                    a[x] = i
    if a == b:
        cnt += 1
print(cnt)