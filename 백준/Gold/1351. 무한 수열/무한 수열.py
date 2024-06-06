import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())

a = dict()
a[0] = 1

def f(n):
    if n in a.keys():
        return a[n]
    a[n] = f(n//p) + f(n//q)
    return a[n]
print(f(n))