arr = [[0] * 100 for _ in range(100)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, 10+a):
        for j in range(b, 10+b):
            arr[i][j] = 1
print(sum(sum(arr[x]) for x in range(100)))