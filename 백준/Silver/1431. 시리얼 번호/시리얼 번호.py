import re
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

def f(s):
    return sum(map(int, re.sub('[A-Z]', '0', s)))

for i in range(n, 0, -1):
    for x in range(-1, -i, -1):
        a, b = arr[x-1], arr[x]
        if len(a) != len(b):
            if len(a) > len(b):
                arr[x-1], arr[x] = arr[x], arr[x-1]
            continue
        elif f(a) != f(b):
            if f(a) > f(b):
                arr[x-1], arr[x] = arr[x], arr[x-1]
            continue
        elif a > b:
            arr[x-1], arr[x] = arr[x], arr[x-1]
            continue

for a in arr:
    print(a)