import sys
import heapq
input = sys.stdin.readline

def f():
    node = [float('inf')] * (N+1)
    node[0] = 0

    for i in range(1, N + 1):
        edge.append((0, i, 0))
    
    for _ in range(N):
        c = []
        for s, e, t in edge:
            if node[s] + t < node[e]:
                c.append((e, node[s] + t))
        for i, v in c:
            node[i] = min(node[i], v)

    for s, e, t in edge:
        if node[s] + t < node[e]:
            return 'YES'

    return 'NO'

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edge = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edge.append((S, E, T))
        edge.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edge.append((S, E, -T))

    print(f())