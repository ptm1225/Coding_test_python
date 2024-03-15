from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0:
        print(0)
    else:
        d = defaultdict(int)
        for _ in range(n):
            name, kind = input().split()
            d[kind] += 1
        print(eval('*'.join([str(i+1) for i in d.values()]))-1)