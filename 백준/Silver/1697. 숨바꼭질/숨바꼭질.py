n, k = map(int, input().split())

if n >= k:
    print(n-k)
else:
    visited = [False] * 100001
    visited[n] = True
    count = 0
    queue = [n]
    while queue:
        for _ in range(len(queue)):
            v = queue.pop(0)
            if v == k:
                queue.clear()
                print(count)
                break
            for i in [-1, 1, v]:
                next = v + i
                if 0 <= next <= 100000 and not visited[next]:
                    visited[next] = True
                    queue.append(next)
        count += 1