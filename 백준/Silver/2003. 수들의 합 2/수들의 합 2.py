import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

i, j = 0, 1
cnt = 0

while i <= j <= N:
    x = sum(A[i:j])
    if x > M:
        i += 1
    elif x < M:
        j += 1
    else:
        cnt += 1
        j += 1
print(cnt)