inp = int(input())
a = [['*'] * inp for i in range(inp)]

def func(n):
  if n == 1:
    pass
  else:
    for x in range(inp//n):
      for i in range(n//3 + x*n, (2*n)//3 + x*n):
        for y in range(inp//n):
          for j in range(n//3 + y*n, (2*n)//3 + y*n):
            a[i][j] = ' '
    func(n//3)

func(inp)

for i in range(inp):
  for j in range(inp):
    print(a[i][j], end = '')
  print()