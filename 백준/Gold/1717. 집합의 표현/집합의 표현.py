import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [i for i in range(n + 1)]

def find_arr(x):
    if arr[x] != x:
        arr[x] = find_arr(arr[x])
    return arr[x]

def union(a, b):
    a_arr = find_arr(a)
    b_arr = find_arr(b)
    if a_arr < b_arr:
        arr[b_arr] = a_arr
    else:
        arr[a_arr] = b_arr

for _ in range(m):
    z, a, b = map(int, input().rstrip().split())
    if z == 0:
        union(a, b)
    elif z == 1:
        print('YES' if find_arr(a) == find_arr(b) else 'NO')