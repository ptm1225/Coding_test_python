N = int(input())
A = list(map(int, input().split()))

i, j = 0, N-1
result = float('inf')

while i < j:
    v = A[i] + A[j]
    if v < 0:
        i += 1
    elif v > 0:
        j -= 1
    else:
        result = 0
        break

    if abs(result) > abs(v):
        result = v

print(result)