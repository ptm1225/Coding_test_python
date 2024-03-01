n = int(input())
m = int(input())
broken = set(input().split()) if m else set()

count = abs(n - 100)

for num in range(1000001):
    for i in str(num):
        if i in broken:
            break
    else:
        count = min(count, len(str(num))+abs(n-num))

print(count)