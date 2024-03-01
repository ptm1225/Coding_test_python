from math import ceil
t = int(input())
result = []
for _ in range(t):
    x, y = map(int, input().split())
    diff = y-x
    if diff < 3:
        result.append(diff)
    else:
        n = ceil(diff**0.5)
        if diff < ((n-1)**2+n**2)/2:
            result.append(2*n-2)
        else:
            result.append(2*n-1)
for r in result:
    print(r)