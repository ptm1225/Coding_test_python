import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    if n < 4:
        print(n)
        continue
    
    dp = [[0, 0] for _ in range(n+1)]
    dp[1] = [1, 0]
    dp[2] = [1, 1]
    dp[3] = [2, 1]
    for i in range(4, n+1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-2][1]
        if i % 3 == 0:
            dp[i][1] += 1
    print(sum(dp[n]))