total = 0
x = 0
b = ['D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']

for _ in range(20):
  name, n, degree = input().split()
  
  if degree == 'P':
    continue
  
  n = int(n[0])
  x += n
  
  if degree == 'F':
    total += n * 0
  else:
    for i, v in enumerate(b):
      if v == degree:
        total += n * (1 + 0.5 * i)
        break

print('{0:.6f}'.format(total/x))