import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

black = []
white = []

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            black.append((i, j))
        else:
            white.append((i, j))

def backtrack(bishops, diagonals1, diagonals2, idx, positions):
    if idx == len(positions):
        return bishops

    x, y = positions[idx]
    max_bishops = 0

    if arr[x][y] == 1 and not diagonals1[x + y] and not diagonals2[x - y + n - 1]:
        diagonals1[x + y] = True
        diagonals2[x - y + n - 1] = True
        max_bishops = max(max_bishops, backtrack(bishops + 1, diagonals1, diagonals2, idx + 1, positions))
        diagonals1[x + y] = False
        diagonals2[x - y + n - 1] = False

    max_bishops = max(max_bishops, backtrack(bishops, diagonals1, diagonals2, idx + 1, positions))
    return max_bishops

diagonals1_black = [False] * (2 * n - 1)
diagonals2_black = [False] * (2 * n - 1)
diagonals1_white = [False] * (2 * n - 1)
diagonals2_white = [False] * (2 * n - 1)

max_black = backtrack(0, diagonals1_black, diagonals2_black, 0, black)
max_white = backtrack(0, diagonals1_white, diagonals2_white, 0, white)

print(max_black + max_white)
