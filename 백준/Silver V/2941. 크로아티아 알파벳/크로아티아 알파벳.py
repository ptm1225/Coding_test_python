st = input()
count = len(st)

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for v in arr:
  for i in range(len(st)):
    if st[i:i+len(v)] == v:
      count -= 1

print(count)