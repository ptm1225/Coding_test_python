import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

a, b, c = arr[0], arr[1], arr[2]
for k in range(N-2):
    i, j = k+1, N-1
    left, right = arr[i], arr[j]
    while i < j:
        x = arr[i] + arr[j] + arr[k]
        if abs(x) < abs(left + right + arr[k]):
            left, right = arr[i], arr[j]

        if x > 0:
            j -= 1
        elif x < 0:
            i += 1
        else:
            break
    if abs(arr[k]+left+right) < abs(a+b+c):
        a, b, c = arr[k], left, right
print(a, b, c)