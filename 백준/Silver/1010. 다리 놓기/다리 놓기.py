def fac(n):
  if n < 3:
    return n
  return eval('*'.join(map(str, [i for i in range(1, n+1)])))

result = []
t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  if n == m:
    result.append(1)
  else:
    result.append(fac(m) / (fac(n) * fac(m-n)))

for r in result:
  print(int(r))