a, b, n = map(int, input().split())
a %= b
a *= 10
arr = []
while n:
  arr.append(a//b)
  a %= b
  a *= 10
  n -= 1

print(arr[-1])