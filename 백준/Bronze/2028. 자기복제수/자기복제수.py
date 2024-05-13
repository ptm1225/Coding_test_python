t = int(input())
for _ in range(t):
    n = int(input())
    
    s = str(n ** 2)
    if str(n) == s[len(s)-len(str(n)):]:
        print('YES')
    else:
        print('NO')