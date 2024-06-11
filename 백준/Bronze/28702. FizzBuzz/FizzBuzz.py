import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

value = 0
idx = 0
for i,v in enumerate([a, b, c]):
    if v[0] in '0123456789':
        value = int(v)
        idx = i

value += (3-idx)

if value % 3 == 0 and value % 5 == 0:
    print('FizzBuzz')
elif value % 3 == 0 and value % 5 != 0:
    print('Fizz')
elif value % 3 != 0 and value % 5 == 0:
    print('Buzz')
else:
    print(value)