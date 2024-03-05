N, m, M, T, R = map(int, input().split())

X = m
result = 0
if X + T > M:
    result = -1
else:
    while N:
        if X+T <= M:
            X += T
            N -= 1
        elif X >= m:
            X = X - R if X - R >= m else m
        result += 1

print(result)