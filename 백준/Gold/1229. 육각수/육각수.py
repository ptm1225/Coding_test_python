import sys
input = sys.stdin.readline

n = int(input())
arr = [1, 6]

for i in range(2, 707):
    arr.append(arr[i-1] + 4*i + 1)

dp = [0] + [7] * n
for i in arr:
    for j in range(i, n+1):
        dp[j] = min(dp[j], dp[j-i] + 1)
print(dp[n])