n = int(input())
arr = list(map(int, input().split()))
r = int(input())
count = 0
for i, v in enumerate(arr):
    if r == v:
        count += 1
print(count)