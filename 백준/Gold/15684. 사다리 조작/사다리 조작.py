import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
arr = [[0]*(N+1) for _ in range(H+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1

result = 4

def check():
    for i in range(1, N+1):
        tmp = i
        for j in range(1, H+1):
            if arr[j][tmp-1] == 1:
                tmp -= 1
            elif arr[j][tmp] == 1:
                tmp += 1
        if i != tmp:
            return False
    return True

def bt(cnt, start_x, start_y):
    global result
    if cnt >= result:
        return

    if check():
        result = cnt
        return

    for x in range(start_x, H+1):
        for y in range(1 if x != start_x else start_y, N):
            if arr[x][y] == 0 and arr[x][y-1] == 0 and arr[x][y+1] == 0:
                arr[x][y] = 1
                bt(cnt + 1, x, y + 2)
                arr[x][y] = 0

bt(0, 1, 1)

if result > 3:
    print(-1)
else:
    print(result)