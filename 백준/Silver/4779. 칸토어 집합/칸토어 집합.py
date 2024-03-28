import sys
input = sys.stdin.readline
def f(s, i, n):
    if n == 0:
        return
    for x in range(i+3**(n-1), i+2*3**(n-1)):
        s[x] = ' '
    f(s, i, n-1)
    f(s, i+2*3**(n-1), n-1)
while True:
    n = input().rstrip()
    if n == '':
        break
    n = int(n)
    s = ['-'] * 3**n
    f(s, 0, n)
    print(''.join(s))