n, m = map(int, input().split())

visited = [0] * n

def dfs(idx, cnt):
    if cnt == m:
        for i, v in enumerate(visited):
            for _ in range(v):
                print(i+1, end=' ')
        print()

    else:
        for i in range(idx, n):
            visited[i] += 1
            dfs(i, cnt+1)
            visited[i] -= 1

dfs(0, 0)