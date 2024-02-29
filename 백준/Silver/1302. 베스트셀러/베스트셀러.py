from collections import Counter
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
d = Counter(arr)
m = max(d.values())
result = []
for k, v in d.items():
    if v == m:
        result.append(k)
print(sorted(result)[0])