n = int(input())
steps = input()

arr = [['#'] * (2*n+1) for _ in range(2*n+1)]
dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]

cx, cy = n, n
i = 0
arr[n][n] = '.'

for step in steps:
    if step == 'L':
        i = (i+1) % 4
    elif step == 'R':
        i = i-1 if i > 0 else 3
    elif step == 'F':
        cx += dr[i][0]
        cy += dr[i][1]
        arr[cx][cy] = '.'


start_x, end_x, start_y, end_y = 0, 0, 0, 0

for i in range(2*n+1):
    if '.' in arr[i]:
        start_x = i
        break
for i in range(-1, -(2*n+2), -1):
    if '.' in arr[i]:
        end_x = i
        break

is_r = False
for j in range(2*n+1):
    for i in range(2*n+1):
        if arr[i][j] == '.':
            start_y = j
            is_r = True
            break
    if is_r:
        break
is_r = False
for j in range(-1, -(2*n+2), -1):
    for i in range(-1, -(2*n+2), -1):
        if arr[i][j] == '.':
            end_y = j
            is_r = True
            break
    if is_r:
        break

for i in range(start_x, 2*n+end_x+2):
    for j in range(start_y, 2*n+end_y+2):
        print(arr[i][j], end='')
    if i < 2*n+end_x+1:
        print()