n = int(input())
arr = []
for _ in range(n):
    arr.append(input().split())

result = []
for i in range(n):
    count = 0
    v = []
    for j in range(5):
        for k in range(n):
            if i != k and arr[i][j] == arr[k][j] and k not in v:
                count += 1
                v.append(k)
    result.append(count)

m = max(result)
for i, v in enumerate(result):
    if v == m:
        print(i+1)
        break