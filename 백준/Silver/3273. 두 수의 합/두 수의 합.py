import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
cnt = 0
i, j = 0, n-1
while i < j:
    if arr[i] + arr[j] < x:
        i += 1
    elif arr[i] + arr[j] > x:
        j -= 1
    else:
        i += 1
        j -= 1
        cnt += 1
print(cnt)