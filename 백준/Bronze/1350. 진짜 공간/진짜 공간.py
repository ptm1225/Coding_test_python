n = int(input())
arr = list(map(int, input().split()))
d = int(input())
result = 0
for f in arr:
    if f == 0:
        continue

    if f <= d:
        result += d
    elif f % d == 0:
        result += f
    else:
        result += d * (f//d + 1)
print(result)