n = int(input())
arr = list(map(int, input().split()))
result = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j:
            g = (arr[i] - arr[j]) / (i - j)
            C = arr[i] - g * i
            if i > j:
                if all([(g*k + C) > arr[k] for k in range(j+1, i)]):
                    cnt += 1
            else:
                if all([(g*k + C) > arr[k] for k in range(i+1, j)]):
                    cnt += 1
    result = max(result, cnt)
print(result)