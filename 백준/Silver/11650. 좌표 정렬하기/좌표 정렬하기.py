n = int(input())
arr = [[] for _ in range(200001)]
for _ in range(n):
    x, y = map(int, input().split())
    arr[x].append(y)

for i in range(-100000, 100001):
    for x in sorted(arr[i]):
        print(i, x)