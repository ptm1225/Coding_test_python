six = []
one = []
n, m = map(int, input().split())
for _ in range(m):
  x, y = map(int, input().split())
  six.append(x)
  one.append(y)

if min(six) > min(one) * 6:
  money = min(one) * n
else:
  money = min(six) * (n//6)
  if min(six) > min(one) * (n%6):
    money += min(one) * (n%6)
  else:
    money += min(six)

print(money)