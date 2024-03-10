n, m = map(int, input().split())
d = {}
p = {}
for i in range(n):
    x = input()
    d[str(i+1)] = x
    p[x] = str(i+1)

arr = []
for _ in range(m):
    arr.append(input())
for s in arr:
    if s.isdigit():
        print(d[s])
    else:
        print(p[s])