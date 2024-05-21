from itertools import combinations
n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(sum(sorted(arr)[:5]))
else:
    p = [(0,1), (0,2), (0,3), (0,4), (1,2), (1,3), (2,4), (3,4), (5,1), (5,2), (5,3), (5,4)]
    q = [(0,1,2), (0,1,3), (0,3,4), (0,2,4), (5,1,2), (5,1,3), (5,3,4), (5,2,4)]
    one = 4*(n-1)*(n-2) + (n-2)**2
    two = 4*(n-1) + 4*(n-2)
    thr = 4
    o = min(arr)
    s = min([arr[x]+arr[y] for x, y in p])
    t = min([arr[x]+arr[y]+arr[z] for x, y, z in q])
    r = one * o + two * s + thr * t
    print(r)