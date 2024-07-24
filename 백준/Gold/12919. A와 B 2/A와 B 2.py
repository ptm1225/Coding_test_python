import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(T)
    
    while q:
        t = q.popleft()
        if len(t) < n:
            continue
        if t == S:
            return 1
        
        if t[-1] == 'A':
            q.append(t[:-1])
        if t[0] == 'B':
            q.append(t[1:][::-1])
        
    return 0

S = input().rstrip()
T = input().rstrip()
n = len(S)

print(bfs())