t = int(input())

dp = [0] * 101
dp[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(t):
    print(dp[int(input())])