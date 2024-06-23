import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return parent[x]

def union_parent(u, v):
    u = find_parent(u)
    v = find_parent(v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

N, M = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))
edges.sort(key=lambda x:x[2])
parent = list(range(N+1))
mst_cost = []
for u, v, w in edges:
    if find_parent(u) != find_parent(v):
        union_parent(u, v)
        mst_cost.append(w)
mst_cost.pop()
print(sum(mst_cost))