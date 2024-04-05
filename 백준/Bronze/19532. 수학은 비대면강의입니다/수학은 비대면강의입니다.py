a,b,c,d,e,f = map(int, input().split())
x = (c*e - f*b) // (a*e - b*d)
if b != 0:
    y = (c - a*x) // b
else:
    y = (f - d*x) // e
print(x, y)