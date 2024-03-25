n = int(input())
arr = [[0]*n for _ in range(n)]
m = []
for _ in range(n):
    m.append(input())

di = [1,1,1,0,0,-1,-1,-1]
dj = [-1,0,1,-1,1,-1,0,1]

for i in range(n):
    for j in range(n):
        if m[i][j] != '.':
            x = int(m[i][j])
            for d in range(8):
                if 0<=i+di[d]<n and 0<=j+dj[d]<n:
                    arr[i+di[d]][j+dj[d]] += x

for i in range(n):
    for j in range(n):
        if m[i][j] != '.':
            print('*', end='')
        elif arr[i][j] > 9:
            print('M', end='')
        else:
            print(arr[i][j], end='')
    print()