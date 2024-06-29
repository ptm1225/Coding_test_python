import sys
input = sys.stdin.readline

N = int(input())
arr = []
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
dp = [0] * N

for i in range(N-1):
    for j in range(i+1, N):
        if i + T[i] <= j:
            dp[j] = max(dp[j], dp[i] + P[i])
for i in range(N):
    if i + T[i] <= N:
        dp[i] += P[i]
print(max(dp))