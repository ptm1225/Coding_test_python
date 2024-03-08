n = int(input())
r = n - (len(str(n))*9)

while r < n:
    if eval('+'.join(str(r))) + r == n:
        break
    r += 1

if r == n:
    print(0)
else:
    print(r)