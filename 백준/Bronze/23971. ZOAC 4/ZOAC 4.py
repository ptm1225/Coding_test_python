h, w, n, m = map(int, input().split())
s = 0

for i in range(0, h, n+1):
    for j in range(0, w, m+1):
        s += 1
print(s)