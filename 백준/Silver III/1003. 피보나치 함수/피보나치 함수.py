n = int(input())
result = []
for _ in range(n):
  number = int(input())
  if number == 0:
    result.append((1, 0))
  elif number == 1:
    result.append((0, 1))
  else:
    arr = []
    
    for i in range(number):
      if len(arr) < 2:
        arr.append(1)
      else:
        arr.append(arr[i-1] + arr[i-2])
    result.append((arr[-2], arr[-1]))

for a, b in result:
  print(a, b)