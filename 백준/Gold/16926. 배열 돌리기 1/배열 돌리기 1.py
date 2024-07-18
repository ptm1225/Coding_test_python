import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    tmp = [[0]*M for _ in range(N)]
    for l in range(max(N, M)//2):
        a = N-(2*l+1)
        b = M-(2*l+1)
        if a < 1 or b < 0:
            break
        for j in range(a):
            tmp[j+l+1][l] = A[j+l][l]
            tmp[N-2-j-l][M-1-l] = A[N-1-j-l][M-1-l]
        
        for j in range(b):
            tmp[N-1-l][j+l+1] = A[N-1-l][j+l]
            tmp[l][M-2-j-l] = A[l][M-1-j-l]
    
    A = tmp

for a in A:
    print(*a)