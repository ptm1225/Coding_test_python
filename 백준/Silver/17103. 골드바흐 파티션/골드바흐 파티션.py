import sys
input = sys.stdin.readline

z = 1000000
arr = [False, False] + [True] * (z-1)
for i in range(2, int(z**0.5)+1):
    if arr:
        for x in range(2*i, z+1, i):
            arr[x] = False

t = int(input())
for _ in range(t):
    n = int(input())
    i = 2
    cnt = 0
    while i <= n//2:
        if arr[i] and arr[n-i]:
            cnt += 1
        i += 1
    print(cnt)