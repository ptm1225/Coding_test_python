a,b = map(int, input().split())

n = 1
arr = []
while n < 101:
    arr = arr + [n] * n
    n += 1

print(sum(arr[a-1:b]))