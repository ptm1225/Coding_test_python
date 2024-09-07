n = int(input())
arr = [input() for _ in range(n)]
for x in arr:
    if len(x) > 1:
        print(x[0].upper() + x[1:])
    else:
        print(x[0].upper())