import sys
input = sys.stdin.readline
from collections import deque

def BFS(v,time):
    visited[v] = True
    queue = deque()
    queue.append((v,time))
    answer = 100001
    while queue:
        now = queue.popleft()
        if now[0] == K:
            answer = min(answer, now[1])

        a = now[0]*2 # 1번
        if a <= 100000 and not visited[a]:
            visited[a] = True
            queue.append((a,now[1]))
        b = now[0]-1 # 2번
        if b >= 0 and not visited[b]:
            visited[b] = True
            queue.append((b,now[1]+1))
        c = now[0]+1 # 3번
        if c <= 100000 and not visited[c]:
            visited[c] = True
            queue.append((c,now[1]+1))

    return answer


N, K = map(int, input().split())
visited = [False for _ in range(100001)]
answer = BFS(N,0)
print(answer)