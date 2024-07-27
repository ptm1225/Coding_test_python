import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        i = 1
        while True:
            x = int('1'*i)
            if x % n == 0:
                break
            i += 1
        print(i)
    except:
        break