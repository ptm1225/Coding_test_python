import sys
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
edge = []
for _ in range(E):
    edge.append(tuple(map(int, input().split())))
edge.sort(key=lambda x: x[2])

s = [i for i in range(V + 1)]

def find(v):
    if v == s[v]:
        return v
    else:
        s[v] = find(s[v])
        return s[v]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if a < b:
            s[b] = a
        else:
            s[a] = b

cnt = 0
for e in edge:
    u, v, w = e
    if find(u) != find(v):
        union(u, v)
        cnt += w
print(cnt)