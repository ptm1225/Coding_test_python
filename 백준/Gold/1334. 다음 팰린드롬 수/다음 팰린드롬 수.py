n = input()
m = len(n) // 2

if len(n) == 1:
    t = int(n) + 1
    if t > 9:
        print('11')
    else:
        print(str(t))
else:
    if len(n) % 2 == 0:
        t = n[:m]
        if int(t[::-1]) > int(n[m:]):
            print(t + t[::-1])
        else:
            t = str(int(t) + 1)
            if len(t) > m:
                t = t[:m]
                print(t + '0' + t[::-1])
            else:
                print(t + t[::-1])
    else:
        t = n[:m]
        if int(t[::-1]) > int(n[m+1:]):
            print(t + n[m] + t[::-1])
        else:
            mid = int(n[m]) + 1
            if mid > 9:
                t = str(int(t) + 1)
                if len(t) > m:
                    print(t + t[::-1])
                else:
                    print(t + '0' + t[::-1])
            else:
                print(t + str(mid) + t[::-1])