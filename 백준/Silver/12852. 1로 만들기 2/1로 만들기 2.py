import sys
input = sys.stdin.readline

def f(x):
    if x == arr[x]:
        print(1)
        return
    print(x, end=' ')
    return f(arr[x])

N = int(input())
dp = [float('inf')] * (N+1)
arr = list(range(N+1))
dp[1] = 0

for x in range(2, N+1):
    if x % 3 == 0:
        if dp[x] > dp[x//3] + 1:
            dp[x] = dp[x//3] + 1
            arr[x] = x//3
    if x % 2 == 0:
        if dp[x] > dp[x//2] + 1:
            dp[x] = dp[x//2] + 1
            arr[x] = x//2
    if dp[x] > dp[x-1] + 1:
        dp[x] = dp[x-1] + 1
        arr[x] = x-1

print(dp[N])
f(N)