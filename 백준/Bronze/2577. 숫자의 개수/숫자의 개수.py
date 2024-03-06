from collections import Counter
r = 1
for _ in range(3):
    r *= int(input())
c = Counter(str(r))
for i in range(10):
    if str(i) in c.keys():
        print(c[str(i)])
    else:
        print(0)