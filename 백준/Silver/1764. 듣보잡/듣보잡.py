n, m = map(int, input().split())
d = []
b = []
for _ in range(n):
    d.append(input())
for _ in range(m):
    b.append(input())
s = sorted(list(set(b) & set(d)))
print(len(s))
for x in s:
    print(x)