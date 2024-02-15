arr = []

n = int(input())
for _ in range(n):
  arr.append(input())

for word in arr:
  t = ''
  d = []
  for v in word:
    if v not in d:
      d.append(v)
      t = v
    elif t != v:
      n -= 1
      break
  
print(n)