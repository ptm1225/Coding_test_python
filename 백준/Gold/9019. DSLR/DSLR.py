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
        D = 2*v if 2*v <= 9999 else (2*v)%10000
        S = v-1 if v != 0 else 9999
        L = (v%1000)*10 + v//1000
        R = (v%10)*1000 + v//10
        if not visited[D]:
            visited[D] = True
            q.append((D, s+'D'))
        if not visited[S]:
            visited[S] = True
            q.append((S, s+'S'))
        if not visited[L]:
            visited[L] = True
            q.append((L, s+'L'))
        if not visited[R]:
            visited[R] = True
            q.append((R, s+'R'))
    print(ans)