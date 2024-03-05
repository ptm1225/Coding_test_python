n = int(input())
y = 0
m = 0
arr = list(map(int, input().split()))
for i in arr:
    y += (i//30+1) * 10
    m += (i//60+1) * 15
if y == m:
    print('Y','M',y)
elif y < m:
    print('Y', y)
else:
    print('M', m)