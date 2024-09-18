n = int(input())
P = [-1] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = P[i]
    for k in range(1, i):
        dp[i] = max(dp[i], dp[i-k] + P[k])

print(dp[n])