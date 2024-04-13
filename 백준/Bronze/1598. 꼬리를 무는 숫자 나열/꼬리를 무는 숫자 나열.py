from math import ceil
a, b = map(int, input().split())
if b > a:
    x = (ceil(b/4) - ceil(a/4))
    print(x + abs(a - (b-4*x)))
else:
    x = (ceil(a/4) - ceil(b/4))
    print(x + abs(b - (a-4*x)))