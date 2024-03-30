n, m = map(int, input().split())
A = []
B = []
for _ in range(n):
    A.append(list(map(int, input().split())))
m, k = map(int, input().split())
for _ in range(m):
    B.append(list(map(int, input().split())))

C = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        t = 0
        for l in range(m):
            t += A[i][l] * B[l][j]
        C[i][j] = t

for x in C:
    print(*x)