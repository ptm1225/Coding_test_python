import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == '0':
        break

    l = len(n)
    cnt = 0
    while True:
        if n == n[::-1]:
            break
        n = f'{(int(n)+1):0{l}d}'
        cnt += 1
    print(cnt)