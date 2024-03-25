from itertools import combinations as c
n = int(input())
arr = [1] * 21
for i in range(2, 21):
    arr[i] = i * arr[i-1]
z = False
for i in range(1, 21):
    for x in c(arr, i):
        if sum(x) == n:
            z = True
            break
    if z:
        break
if z:
    print('YES')
else:
    print('NO')