from itertools import permutations
N = int(input())
A = list(map(int, input().split()))

result = 0
for B in permutations(A, N):
    result = max(result, sum(abs(B[i] - B[i+1]) for i in range(N-1)))
print(result)