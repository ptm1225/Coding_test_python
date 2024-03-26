n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
v = [0] * 10001

def f(idx, cnt):
    if cnt == m:
        for i in range(10001):
            if v[i]:
                for x in range(v[i]):
                    print(i, end=' ')
        print()
    else:
        for i in arr:
            if i >= idx:
                v[i] += 1
                f(i, cnt+1)
                v[i] -= 1
                
f(min(arr), 0)