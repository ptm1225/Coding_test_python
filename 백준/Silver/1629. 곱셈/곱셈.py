a, b, c = map(int, input().split())

result = 1
while b:
    if b%2 != 0:
        result *= a
        result %= c
    a *= a
    a %= c
    b //= 2
print(result)