import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        if i < N-3:
            result = max(result, sum(arr[x][j] for x in range(i, i+4)))
        if j < M-3:
            result = max(result, sum(arr[i][j:j+4]))
        if i < N-1 and j < M-1:
            result = max(result, sum(sum(arr[x][j:j+2]) for x in range(i, i+2)))
        if i < N-2 and j < M-1:
            result = max(result, sum(arr[x][j] for x in range(i, i+3)) + arr[i+2][j+1])
            result = max(result, sum(arr[x][j] for x in range(i, i+3)) + arr[i][j+1])
            result = max(result, sum(arr[x][j+1] for x in range(i, i+3)) + arr[i+2][j])
            result = max(result, sum(arr[x][j+1] for x in range(i, i+3)) + arr[i][j])
            result = max(result, arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1])
            result = max(result, arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j])
            result = max(result, sum(arr[x][j] for x in range(i, i+3)) + arr[i+1][j+1])
            result = max(result, sum(arr[x][j+1] for x in range(i, i+3)) + arr[i+1][j])
        if i < N-1 and j < M-2:
            result = max(result, sum(arr[i][j:j+3]) + arr[i+1][j])
            result = max(result, sum(arr[i][j:j+3]) + arr[i+1][j+2])
            result = max(result, sum(arr[i+1][j:j+3]) + arr[i][j])
            result = max(result, sum(arr[i+1][j:j+3]) + arr[i][j+2])
            result = max(result, arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2])
            result = max(result, arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] + arr[i][j+2])
            result = max(result, sum(arr[i][j:j+3]) + arr[i+1][j+1])
            result = max(result, sum(arr[i+1][j:j+3]) + arr[i][j+1])
print(result)