n = int(input())
num = [0] * 20000001
arr = list(map(int, input().split()))
for a in arr:
    num[a] = 1
m = int(input())
check = list(map(int , input().split()))

for c in check:
    print(num[c], end=' ')