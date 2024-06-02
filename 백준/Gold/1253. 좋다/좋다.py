import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

if n == 2:
    print(0)
else:
    A.sort()
    cnt = 0
    for idx in range(n):
        i, j = 0, n-1
        while i < j:
            s = A[i] + A[j]
            if s < A[idx]:
                i += 1
            elif s > A[idx]:
                j -= 1
            else:
                if i == idx:
                    i += 1
                elif j == idx:
                    j -= 1
                else:
                    cnt += 1
                    break
    print(cnt)