arr = [['']*15 for _ in range(5)]
for i in range(5):
    for j, v in enumerate(input()):
        arr[i][j] = v

for j in range(15):
    for i in range(5):
        print(arr[i][j], end='')