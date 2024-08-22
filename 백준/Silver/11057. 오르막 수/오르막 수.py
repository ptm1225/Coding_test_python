n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1

for k in range(2, n+1):
    for i in range(10):
        dp[k][i] = sum(dp[k-1][j] for j in range(i+1)) % 10007

print(sum(dp[n]) % 10007)