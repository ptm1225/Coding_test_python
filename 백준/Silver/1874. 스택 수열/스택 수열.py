n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
process = []
result = []
number = 1
for i in arr:
    if i >= number: # stack에 원하는 숫자가 없는 경우
        while i >= number:
            stack.append(number)
            process.append('+')
            number += 1
        result.append(stack.pop())
        process.append('-')
    else: # stack에 원하는 숫자가 있는 경우
        s = 0
        while stack and i != s:
            s = stack.pop()
            result.append(s)
            process.append('-')

if arr == result:
    for p in process:
        print(p)
else:
    print('NO')