n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

def func(f, arr):
    count = 0
    s = 'W' if f == 'B' else 'B'
    
    for x in range(8):
        if x % 2 == 0:
            count += arr[x][0:8:2].count(s) + arr[x][1:8:2].count(f)
        else:
            count += arr[x][0:8:2].count(f) + arr[x][1:8:2].count(s)
    
    return count

result = []
for i in range(n-7):
    for j in range(m-7):
        result.append(func('B', [arr[i+x][j:j+8] for x in range(8)]))
        result.append(func('W', [arr[i+x][j:j+8] for x in range(8)]))

print(min(result))