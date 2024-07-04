import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
M = int(input())
dp = [0] * 51

for i in range(1, 51):
    for idx, val in enumerate(P):
        if i - val >= 0:
            dp[i] = max(dp[i], dp[i-val]*10 + idx)
print(dp[M])