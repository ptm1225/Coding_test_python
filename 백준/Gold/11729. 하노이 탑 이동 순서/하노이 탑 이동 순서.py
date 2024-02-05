inp = int(input())

seq = []
count = 0

def f(n, start, mid, end):
  global count
  if n == 1:
    count += 1
    seq.append(f'{start} {end}')
    return
  f(n-1, start, end, mid) # 1 -> 2로 n-1개를 3을 mid로 두고 보냄
  
  count += 1
  seq.append(f'{start} {end}') # 제일 큰 n 원판을 1 -> 3
  
  f(n-1, mid, start, end) # 2 -> 3으로 n-1개를 1을 mid로 두고 보냄

f(inp, 1, 2, 3)

print(count)
for s in seq:
  print(s)