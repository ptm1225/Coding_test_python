import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    i = int(input())
    if i <= k:
        coin.append(i)

if len(coin) == 0:
    print(0)
else:
    dp = [0] * (k+1)
    for c in coin:
        dp[c] += 1
        for i in range(c+1, k+1):
            dp[i] += dp[i-c]
    print(dp[k])