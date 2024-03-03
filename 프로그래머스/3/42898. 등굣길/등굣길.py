def solution(m, n, puddles):
    arr = [[1] * m for _ in range(n)]
    count = 0
    for puddle in puddles:
        i, j = puddle
        arr[j-1][i-1] = 0
    
    for i in range(m):
        if arr[0][i] == 0:
            for j in range(i, m):
                arr[0][j] = 0
            break

    for i in range(n):
        if arr[i][0] == 0:
            for j in range(i, n):
                arr[j][0] = 0
            break
    
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] != 0:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
    
    return arr[-1][-1] % 1000000007