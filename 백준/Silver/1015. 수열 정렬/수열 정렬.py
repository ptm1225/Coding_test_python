n = int(input())
arr = list(map(int, input().split()))
result = [0] * n
x = 0
while x < n:
    i = arr.index(min(arr))
    result[i] = x
    arr[i] = 1001
    x += 1
print(*result)