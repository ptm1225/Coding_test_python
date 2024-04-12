n, m = map(int, input().split())
visited = [False] * (n+1)
arr = []
def f(cnt):
    if cnt == m:
        print(*arr)
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                arr.append(i)
                f(cnt+1)
                visited[i] = False
                arr.pop()
f(0)