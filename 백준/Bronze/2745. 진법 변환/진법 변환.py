s, n = input().split()
n = int(n)
result = 0
for i, x in enumerate(s[::-1]):
    if x not in '0123456789':
        x = ord(x) - 55
    else:
        x = int(x)
    result += x * n ** i
print(result)