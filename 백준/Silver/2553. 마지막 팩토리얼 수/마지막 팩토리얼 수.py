import math
n = int(input())
fact = str(math.factorial(n))
for i in fact[::-1]:
    if i != '0':
        print(i)
        break