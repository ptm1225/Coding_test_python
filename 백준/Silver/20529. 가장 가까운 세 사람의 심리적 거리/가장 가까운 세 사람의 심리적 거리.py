t = int(input())
for _ in range(t):
    n = int(input())
    s = input().split()
    if n <= 32:
        m = 100
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    tmp = sum([x!=y for x, y in zip(s[i], s[j])])
                    tmp += sum([x!=y for x, y in zip(s[j], s[k])])
                    tmp += sum([x!=y for x, y in zip(s[k], s[i])])
                    m = min(m, tmp)
        print(m)
    else:
        print(0)