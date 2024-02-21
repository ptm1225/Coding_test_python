n = int(input())
arr = [[] for _ in range(51)]
for _ in range(n):
    x = input()
    if x not in arr[len(x)]:
        arr[len(x)].append(x)
    

for a in arr:
    if not len(a):
        continue
    a.sort()
    for i in a:
        print(i)