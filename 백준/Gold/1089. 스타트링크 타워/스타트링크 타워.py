n = int(input())
arr = [input() for _ in range(5)]
d = []

for i in range(0, 4*n, 4):
    if arr[1][i+1] == '#' or arr[3][i+1] == '#':
        print(-1)
        exit()
    
    s = list(range(10))
    for k in range(1, 4):
        if arr[k][i+1] == '#':
            s.remove(0)
            break
    
    for k in range(5):
        if '#' in arr[k][i:i+2]:
            s.remove(1)
            break
    
    if '#' in arr[1][i:i+2] or '#' in arr[3][i+1:i+3]:
        s.remove(2)

    if '#' in arr[1][i:i+2] or '#' in arr[3][i:i+2]:
        s.remove(3)
    
    if arr[0][i+1] == '#' or arr[1][i+1] == '#' or '#' in arr[3][i:i+2] or '#' in arr[4][i:i+2]:
        s.remove(4)
    
    if '#' in arr[1][i+1:i+3] or '#' in arr[3][i:i+2]:
        s.remove(5)
    
    if '#' in arr[1][i+1:i+3] or arr[3][i+1] == '#':
        s.remove(6)
    
    for k in range(1, 5):
        if '#' in arr[k][i:i+2]:
            s.remove(7)
            break
    
    if arr[1][i+1] == '#' or arr[3][i+1] == '#':
        s.remove(8)
    
    if arr[1][i+1] == '#' or '#' in arr[3][i:i+2]:
        s.remove(9)
    
    d.append([s, len(s)])

if n == 1:
    print(sum(d[0][0])/d[0][1])
else:
    result = 0
    for i in range(n):
        a, l = d[i][0], d[i][1]
        w = eval('*'.join(map(str, [d[k][1] for k in range(n) if i != k])))
        for j in range(l):
            result += w * a[j] * (10 ** (n-i-1))

    print(result/eval('*'.join(map(str, [d[k][1] for k in range(n)]))))