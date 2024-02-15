n = int(input())

result = []

for _ in range(n):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  a = (x1-x2) ** 2 + (y1-y2) ** 2
  b = (r1 + r2) ** 2
  a, b = int(a), int(b)
  if a == 0 and r1 == r2:
    result.append(-1)
  elif a == b or abs(r1-r2) ** 2 == a:
    result.append(1)
  elif a < b and abs(r1 - r2)**2 < a:
    result.append(2)
  else:
    result.append(0)

for r in result:
  print(r)