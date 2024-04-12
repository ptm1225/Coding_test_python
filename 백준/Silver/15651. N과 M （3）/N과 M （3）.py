n, m = map(int, input().split())
arr = []
def f(cnt):
    if cnt == m:
        print(*arr)
    else:
        for i in range(1, n+1):
            arr.append(i)
            f(cnt+1)
            arr.pop()
f(0)