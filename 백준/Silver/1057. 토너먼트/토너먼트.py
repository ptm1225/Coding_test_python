n, kim, lim = map(int, input().split())
count = 1

while (kim+1)//2 != (lim+1)//2:
    kim, lim = (kim+1)//2 , (lim+1)//2
    count += 1

print(count)