n = int(input())
i = 1
while True:
    if n > i:
        n -= i
        i += 1
        continue
    else:
        if (i+1) % 2 == 0:
            print(str((i+1)-n) + '/' + str(n))
        else:
            print(str(n) + '/' + str((i+1)-n))
        break