import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

result = 0
i, j = 0, arr[-1] - arr[0]

while i <= j:
    mid = (i+j)//2
    current = arr[0]
    cnt = 1
    for idx in range(1, n):
        if arr[idx] - mid >= current:
            current = arr[idx]
            cnt += 1

    if cnt < c:
        j = mid - 1
    else:
        i = mid + 1
        result = mid
print(result)