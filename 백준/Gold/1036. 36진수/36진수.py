import sys
input = sys.stdin.readline

d = []
for i in range(36):
    d.append([i, 0])

n = int(input())
for _ in range(n):
    s = input().lstrip('0').rstrip()
    l = len(s) - 1
    for i, v in enumerate(s):
        if v in '0123456789':
            d[int(v)][1] += 36 ** (l-i)
        else:
            d[ord(v)-55][1] += 36 ** (l-i)

d.sort(key=lambda x:(35*x[1] - x[0]*x[1]), reverse=True)
k = int(input())

for i in range(k):
    d[i][0] = 35

r = 0
for a, b in d:
    r += a*b

result = []
while r > 35:
    result.append(r % 36)
    r //= 36

if r != 0:
    result.append(r)

if len(result) == 0:
    print(0)
else:
    for i in result[::-1]:
        if i < 10:
            print(str(i), end='')
        else:
            print(chr(i+55), end='')