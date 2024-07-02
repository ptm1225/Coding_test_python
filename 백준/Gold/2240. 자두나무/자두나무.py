import sys
input = sys.stdin.readline

T, W = map(int, input().split())
tree = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W+1) for _ in range(T+1)]
c = 0

for i in range(1, T+1):
    t = (c+1) % 2
    if c+1 == tree[i]:
        for j in range(c, W+1, 2):
            dp[i][j] = dp[i-1][j] + 1
        for j in range(t, W+1, 2):
            dp[i][j] = dp[i-1][j]
    else:
        for j in range(t, W+1, 2):
            if j == 0:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        for j in range(c, W+1, 2):
            dp[i][j] = dp[i-1][j]
        c = t
print(max(dp[T]))