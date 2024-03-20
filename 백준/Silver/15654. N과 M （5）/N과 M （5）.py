n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * n
a = []
def dfs(cnt):
    if cnt == m:
        print(*a)
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                a.append(arr[i])
                dfs(cnt+1)
                visited[i] = False
                a.pop()
dfs(0)