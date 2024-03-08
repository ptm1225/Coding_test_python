arr = [[0]*15 for _ in range(15)]
for i in range(15):
    for j in range(1, 15):
        if i == 0:
            arr[i][j] = j
        else:
            arr[i][j] = sum(arr[i-1][:j+1])

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(arr[k][n])