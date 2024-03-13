n = int(input())
arr = list(map(int, input().split()))

d = {}
s = sorted(list(set(arr)))
m = len(s)
for i in range(m):
    if s[i] not in d.keys():
        d[s[i]] = i

print(*[d[i] for i in arr])