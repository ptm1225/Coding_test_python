import sys
input = sys.stdin.readline

M, N = map(int, input().split())
L = list(map(int, input().split()))

i, j = 1, 10 ** 9
result = 0
while i <= j:
    mid = (i+j)//2
    t = sum(x//mid for x in L)
    if t >= M:
        result = max(result, mid)
        i = mid+1
    else:
        j = mid-1

print(result)