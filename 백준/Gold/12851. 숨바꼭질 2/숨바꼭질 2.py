from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0]*100001

dq = deque()
dq.append(n)
visited[n] = 1
cnt = 0 
while dq:
    now = dq.popleft()
    if now == k:
        cnt += 1
        continue
    for nxt in now+1, now-1, now*2:
        if 0 <= nxt <= 100000:
            if visited[nxt] == 0:
                visited[nxt] = visited[now] + 1
                dq.append(nxt)
            elif visited[nxt] == visited[now] + 1:
                dq.append(nxt)

print(visited[k]-1)
print(cnt)