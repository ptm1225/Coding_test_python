n, m = map(int, input().split())
A, B = [], []
for _ in range(n):
    A.append(list(map(int, list(input()))))

for _ in range(n):
    B.append(list(map(int, list(input()))))

def oselo(arr, i, j):
    for x in range(3):
        for y in range(3):
            arr[i+x][j+y] = (arr[i+x][j+y]+1) % 2

count = 0

for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            oselo(A, i, j)
            count += 1

if A != B:
    print(-1)
else:
    print(count)