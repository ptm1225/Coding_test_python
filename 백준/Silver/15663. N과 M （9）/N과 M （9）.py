from collections import defaultdict
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
d = defaultdict(int)

for i in arr:
    d[i] += 1

def f(s, cnt):
    if cnt == m:
        print(*s)
    else:
        for i in d:
            if d[i] == 0:
                continue
            else:
                s.append(i)
                d[i] -= 1
                f(s, cnt+1)
                s.pop()
                d[i] += 1

f([], 0)