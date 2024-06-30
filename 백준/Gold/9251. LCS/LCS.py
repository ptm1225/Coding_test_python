import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
n = len(a)
m = len(b)

dp = [0] * 1000

for i in range(n):
    mx = 0
    for j in range(m):
        if mx < dp[j]:
            mx = dp[j]
        elif a[i] == b[j]:
            dp[j] = mx + 1
print(max(dp))