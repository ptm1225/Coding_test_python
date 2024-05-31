import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
s = 0

for i in range(k):
    s += arr[i]
result = s
for i in range(k, n):
    s += arr[i]
    s -= arr[i-k]
    result = max(result, s)
print(result)