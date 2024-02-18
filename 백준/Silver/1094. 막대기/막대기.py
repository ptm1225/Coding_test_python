x = int(input())
t = 64
arr = [t]
while x != sum(arr):
  a = arr.pop()
  a //= 2
  arr.append(a)
  if sum(arr) < x:
    arr.append(a)

print(len(arr))