n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            s = arr[i] + arr[j] + arr[k]
            if s <= m:
                result = max(result, s)
print(result)