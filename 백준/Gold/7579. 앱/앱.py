import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (sum(c)+1) for _ in range(N+1)]

result = sum(c)
for i in range(1, N+1):
    mem = m[i-1]
    cost = c[i-1]
    for j in range(sum(c)+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + mem)

        if dp[i][j] >= M:
            result = min(result, j)

print(result if M != 0 else 0)