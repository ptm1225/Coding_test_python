import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 100
for i in range(1, n+1):
    dp[i] = dp[i-1] + dp[i-2] if i != 1 else 1
print(dp[n])