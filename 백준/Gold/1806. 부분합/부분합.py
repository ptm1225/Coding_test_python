import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))



if sum(arr) < s:
    print(0)
elif sum([i >= s for i in arr]):
    print(1)
else:
    ps = [arr[0]]
    for i in range(1, n):
        ps.append(ps[i-1] + arr[i])
    
    i, j = 0, 1
    ans = n
    while i < j < n:
        t = ps[j] - ps[i]
        if t < s:
            j += 1
        elif t >= s:
            ans = min(ans, j-i)
            i += 1
    
    print(ans)