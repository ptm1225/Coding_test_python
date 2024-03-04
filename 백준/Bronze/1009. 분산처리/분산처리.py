n = int(input())
result = []
for _ in range(n):
    a, b = map(int, input().split())
    a %= 10
    s = a
    for _ in range(b-1):
        s *= a
        s = int(str(s)[-1])
    result.append(s)
for r in result:
    if r == 0:
        print(10)
    else:
        print(r)