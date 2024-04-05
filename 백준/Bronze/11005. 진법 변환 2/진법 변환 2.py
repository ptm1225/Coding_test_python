s, n = map(int, input().split())
result = ''
while s >= n:
    t = s % n
    result += chr(55+t) if t >= 10 else str(t)
    s //= n
if s:
    result += chr(55+s) if s >= 10 else str(s)
print(result[::-1])