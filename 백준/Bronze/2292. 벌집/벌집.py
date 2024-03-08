t = 1
n = int(input())
result = 0
while n > t:
    t += 6*(result)
    result += 1
if n == 1:
    print(1)
else:
    print(result)