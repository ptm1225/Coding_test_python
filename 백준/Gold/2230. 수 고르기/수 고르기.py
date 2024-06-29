import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
result = float('inf')
i, j = 0, 0
while i <= j < N:
    t = arr[j] - arr[i]
    if t < M:
        j += 1
    elif t >= M:
        result = min(result, t)
        i += 1
print(result)