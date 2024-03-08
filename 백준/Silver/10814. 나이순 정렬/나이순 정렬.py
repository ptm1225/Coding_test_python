n = int(input())
arr = []
for _ in range(n):
    arr.append(input().split())

for a in sorted(arr, key=lambda x:int(x[0])):
    print(*a)