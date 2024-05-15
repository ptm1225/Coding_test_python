n = int(input())

arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

s = arr[0]
total = 0
for i in range(1, n-1):
    a = arr[i]
    b = arr[i+1]
    total += ((a[0]-s[0])*(b[1]-s[1]) - (a[1]-s[1])*(b[0]-s[0])) / 2

print('%.1f'%(abs(total)))