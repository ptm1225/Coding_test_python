import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
m = int(input().rstrip())

dp = [[-1] * n for _ in range(n)]

def f(i, j):
    if i == j:
        return 1
    elif i+1 == j:
        if arr[i] == arr[j]:
            return 1
        else:
            return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        if arr[i] != arr[j]:
            dp[i][j] = 0
        else:
            dp[i][j] = f(i+1, j-1)
        return dp[i][j]
    
for _ in range(m):
    S, E = map(int, input().rstrip().split())
    print(f(S-1, E-1))