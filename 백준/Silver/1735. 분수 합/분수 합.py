from math import gcd
a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = b, d

while f > 0:
    e, f = f, e%f
g = int((a * d + c * b) / e)
h = int(b * d / e)
if g == h:
    g, h = 1, 1
s = gcd(g, h)
print(g//s, h//s)