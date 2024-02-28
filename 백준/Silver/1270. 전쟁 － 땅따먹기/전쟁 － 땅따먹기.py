n = int(input())
result = []
for _ in range(n):
    inp = list(map(int, input().split()))
    total, arr = inp[0], inp[1:]

    count = 0
    m = 0
    for i in arr:
        if count == 0:
            m = i
        if i == m:
            count += 1
        else:
            count -= 1

    t = 0
    for i in arr:
        if m == i:
            t += 1
    if t > total/2:
        print(m)
    else:
        print('SYJKGW')