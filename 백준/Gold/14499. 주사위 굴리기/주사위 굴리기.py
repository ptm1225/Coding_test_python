import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split())) # 동1 서2 북3 남4
dice = [0] * 7
top, bottom = 1, 6

def roll(x, y, dx, dy, a, b, c, d):
    if 0 <= x+dx <= N-1 and 0 <= y+dy <= M-1:
        x, y = x+dx, y+dy
        tmp = dice[a]
        dice[a] = dice[b]
        dice[b] = dice[c]
        dice[c] = dice[d]
        dice[d] = tmp
    return x, y

for num in cmd:
    tmp_x, tmp_y = x, y
    if num == 1:
        x, y = roll(x, y, 0, 1, 6, 3, 1, 4)
    elif num == 2:
        x, y = roll(x, y, 0, -1, 4, 1, 3, 6)
    elif num == 3:
        x, y = roll(x, y, -1, 0, 1, 5, 6, 2)
    elif num == 4:
        x, y = roll(x, y, 1, 0, 2, 6, 5, 1)

    if tmp_x == x and tmp_y == y:
        pass
    else:
        if arr[x][y] == 0:
            arr[x][y] = dice[bottom]
        else:
            dice[bottom] = arr[x][y]
            arr[x][y] = 0
        print(dice[top])