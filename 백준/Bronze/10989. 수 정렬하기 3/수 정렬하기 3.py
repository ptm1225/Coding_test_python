n = int(input())
arr = [0] * 10001
for _ in range(n):
    arr[int(input())] += 1

for i in range(1, 10001):
    for x in range(arr[i]):
        print(i)