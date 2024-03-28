n = int(input())
arr = [0] * n
arr[0], arr[1] = 1, 1
for i in range(2, n):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[n-1], n-2)