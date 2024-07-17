import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

a = [0, 1, 2] * (N//3)
cnt = 0
first = P

while P != a:
    tmp = [0] * N
    for i in range(N):
        tmp[S[i]] = P[i]
    P = tmp
    if P == first:
        print(-1)
        break
    cnt += 1
else:
    print(cnt)