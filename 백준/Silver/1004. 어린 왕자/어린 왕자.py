from math import sqrt

result = []
t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for j in range(n):
        cx, cy, r = map(int, input().split())
        if sqrt((x1-cx)**2+(y1-cy)**2) <= r and sqrt((x2-cx)**2+(y2-cy)**2) > r:
            count += 1
        elif sqrt((x1-cx)**2+(y1-cy)**2) > r and sqrt((x2-cx)**2+(y2-cy)**2) <= r:
            count += 1
    result.append(count)

for r in result:
    print(r)