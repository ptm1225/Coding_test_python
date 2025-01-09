def find_teams(n, arr):
    visited = [False] * n
    finished = [False] * n
    team_count = 0

    def dfs(node):
        nonlocal team_count
        stack = []
        current = node

        while True:
            if visited[current]:
                if not finished[current]:
                    while stack[-1] != current:
                        finished[stack.pop()] = True
                        team_count += 1
                        
                    finished[stack.pop()] = True
                    team_count += 1
                break

            visited[current] = True
            stack.append(current)
            current = arr[current] - 1

        while stack:
            finished[stack.pop()] = True

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return n - team_count

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_teams(n, arr))
