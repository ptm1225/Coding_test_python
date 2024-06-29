import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0] * (N)
for i in range(N):
    dp[i] = A[i]

for i in range(N-1):
    for j in range(i+1, N):
        if A[i] < A[j]:
            dp[j] = max(dp[j], dp[i] + A[j])
print(max(dp))