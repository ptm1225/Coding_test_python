import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] + [float('inf')] * k

for x in coin:
    for i in range(x, k+1):
        dp[i] = min(dp[i-x] + 1, dp[i])

print(dp[k] if dp[k] != float('inf') else -1)