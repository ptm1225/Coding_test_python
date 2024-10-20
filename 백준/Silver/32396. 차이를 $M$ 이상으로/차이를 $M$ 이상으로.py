N, M = map(int, input().split())
A = list(map(int, input().split()))

arr = [abs(A[i + 1] - A[i]) for i in range(N - 1)]
cnt = 0
i = 0

while i < N-1:
    if arr[i] < M:
        cnt += 1
        i += 1
    i += 1

print(cnt)