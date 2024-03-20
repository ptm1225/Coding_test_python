n, m = map(int, input().split())

visited = [False] * n

def dfs(idx, cnt):
    if cnt == m:
        for i, v in enumerate(visited):
            if v:
                print(i+1, end=' ')
        print()

    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(i, cnt+1)
                visited[i] = False

dfs(0, 0)