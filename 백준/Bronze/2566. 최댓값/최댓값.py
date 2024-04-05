arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

result = -1
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if result < arr[i][j]:
            result = arr[i][j]
            x, y = i+1, j+1
print(result)
print(x, y)