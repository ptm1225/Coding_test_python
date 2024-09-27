import sys
sys.setrecursionlimit(100000)

def matrix_mul(A, B, mod):
    N = len(A)
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(N):
                total += A[i][k] * B[k][j]
            result[i][j] = total % mod
    return result

def matrix_pow(matrix, power, mod):
    if power == 1:
        return [[element % mod for element in row] for row in matrix]
    elif power % 2 == 0:
        half = matrix_pow(matrix, power // 2, mod)
        return matrix_mul(half, half, mod)
    else:
        half = matrix_pow(matrix, power - 1, mod)
        return matrix_mul(matrix, half, mod)

def main():
    N, B = input().split()
    N = int(N)
    B = int(B)
    A = [list(map(int, input().split())) for _ in range(N)]
    mod = 1000
    result = matrix_pow(A, B, mod)
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    main()
