import sys
input = sys.stdin.readline

x = input().rstrip()
result = 0

for i, v in enumerate(x[::-1]):
    z = int(v) if v in '0123456789' else ord(v) - 55
    b = z * (16**i)
    result += b
print(result)