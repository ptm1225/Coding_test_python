from collections import Counter
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

print(round(sum(arr) / n))
print(sorted(arr)[n//2])

c = Counter(arr)
mx = max(c.values())
a = []
for k, v in c.items():
    if v == mx:
        a.append(k)
if len(a) == 1:
    print(c.most_common()[0][0])
else:
    print(sorted(a)[1])

print(max(arr) - min(arr))