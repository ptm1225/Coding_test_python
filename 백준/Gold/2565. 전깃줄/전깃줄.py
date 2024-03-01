n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x:x[0])

dp = [1]*n

for i in range(1, n):
  for j in range(0, i):
    if arr[j][1] < arr[i][1]:
      dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))