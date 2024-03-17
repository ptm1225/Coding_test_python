from collections import deque
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b = map(int, input().rstrip().split())
    ans = ''
    q = deque()
    q.append((a, ans))
    visited = [False] * 10000
    while q:
        v, s = q.popleft()
        if v == b:
            ans = s
            break
        if not visited[v]:
            visited[v] = True
            q.append((2*v if 2*v <= 9999 else (2*v)%10000, s+'D'))
            q.append((v-1 if v != 0 else 9999, s+'S'))
            q.append((v*10 if len(str(v)) < 4 else (v%1000)*10 + v//1000, s+'L'))
            q.append(((v%10)*1000 + v//10, s+'R'))
    print(ans)