n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

c = [0] * n
for i in range(n-1):
    for j in range(i+1, n):
        x, y, p, q = arr[i][0], arr[i][1], arr[j][0], arr[j][1]
        if x > p and y > q:
            c[j] += 1
        elif x < p and y < q:
            c[i] += 1

for i in c:
    print(i+1, end=' ')