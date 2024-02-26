n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))

result = []
for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        
        if arr[i][j] == 'Y':
            count += 1
        else:
            for k in range(n):
                if arr[i][k] == arr[j][k] == 'Y':
                    count += 1
                    break
    result.append(count)

print(max(result))