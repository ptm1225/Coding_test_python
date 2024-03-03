n = int(input())
if n < 2:
    print(0)
else:
    num = 1
    for i in range(2, n+1):
        num *= i
    count = 0
    for i in str(num)[::-1]:
        if i != '0':
            break
        count += 1
    print(count)