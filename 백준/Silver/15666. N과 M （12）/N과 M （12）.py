from collections import defaultdict
n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
n = len(arr)

def f(s, cnt):
    if cnt == m:
        print(*s)
    else:
        for i in range(n):
            if cnt == 0 or (s and s[-1] <= arr[i]):
                s.append(arr[i])
                f(s, cnt+1)
                s.pop()

f([], 0)