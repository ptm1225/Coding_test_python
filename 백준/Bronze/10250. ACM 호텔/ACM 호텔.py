from math import ceil
t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        x = h
        y = n//h
    else:
        x = n%h
        y = n//h + 1
    print(x*100+y)