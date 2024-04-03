n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

result = 0
for i in range(1, n+1):
    result = max(result, arr[i-1] * i)
print(result)