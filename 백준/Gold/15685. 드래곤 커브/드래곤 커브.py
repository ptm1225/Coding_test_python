import sys
input = sys.stdin.readline

D = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def f(x, y, g, S, T, cnt):
    if g < cnt:
        return
    
    for d in T:
        x += D[d][0]
        y += D[d][1]
        arr[x][y] = 1

    S = S + T
    T = [(d+1)%4 for d in S[::-1]]
    
    f(x, y, g, S, T, cnt+1)

N = int(input())
arr = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    arr[x][y] = 1
    x += D[d][0]
    y += D[d][1]
    arr[x][y] = 1
    f(x, y, g, [d], [(d+1)%4], 1)

ans = 0
for i in range(100):
    for j in range(100):
        if all([arr[i][j], arr[i+1][j], arr[i][j+1], arr[i+1][j+1]]):
            ans += 1

print(ans)