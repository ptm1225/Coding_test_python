import sys
from math import lcm
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    m, n, x, y = map(int, input().rstrip().split())
    if m < n:
        m, n, x, y= n, m, y, x
    r = lcm(m, n)
    year = x
    ans = 0
    while year <= r:
        t = year%n if year%n != 0 else n
        if t == y:
            ans = year
            break
        year += m
    if ans:
        print(ans)
    else:
        print(-1)