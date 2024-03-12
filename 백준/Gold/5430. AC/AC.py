from collections import deque
t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-1]
    if n > 1:
        arr = arr.split(',')
    d = deque(arr)
    i = 0
    is_error = False
    for x in p:
        if x == 'R':
            i = (i+1)%2
        elif x == 'D':
            if n == 0:
                is_error = True
                break
            if i:
                d.pop()
            else:
                d.popleft()
            n -= 1
    if is_error:
        print('error')
    else:
        if i:
            d.reverse()
        s = ','.join(d)
        print(f'[{s}]')