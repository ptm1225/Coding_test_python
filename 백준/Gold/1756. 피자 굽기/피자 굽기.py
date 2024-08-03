D, N = map(int, input().split())
oven = list(map(int, input().split()))
arr = list(map(int, input().split()))

for i in range(D-1):
    oven[i+1] = min(oven[i], oven[i+1])

for x in arr:
    while oven and oven[-1] < x:
        oven.pop()
    
    if oven:
        oven.pop()
    else:
        print(0)
        exit(0)

print(len(oven)+1)