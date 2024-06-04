import sys
input = sys.stdin.readline

n = int(input())

w = []

for i in range(10):
    w.append([chr(i+65), 0])

not_zero = []
for _ in range(n):
    s = input().rstrip()
    r = len(s)-1
    for i, v in enumerate(s):
        if i == 0:
            not_zero.append(v)
        w[ord(v)-65][1] += 10 ** (r-i)

w.sort(key=lambda x:x[1])

cnt = 0
for s in w:
    if s[1] == 0:
        cnt += 1

result = 0
l = list(range(9, cnt-1, -1))

for s, v in w:
    if v == 0:
        continue
    m = min(l)
    if m == 0 and s in not_zero:
        x = min(set(l)-{0})
        result += x*v
        l.remove(x)
    else:
        result += m * v
        l.remove(m)
print(result)