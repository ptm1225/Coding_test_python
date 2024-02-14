z = ['A', 'B', 'C', 'D', 'E', 'F']

def func(n, number):
    if number == 0:
        return '0'
    arr = []
    while number:
        t = number % n
        number = number//n
        if t >= 10:
            t = z[t-10]
        arr.append(t)
    return ''.join(reversed(list(map(str, arr))))

def solution(n, t, m, p):
    result = []
    for i in range(50000):
        result.append(func(n, i))
    result = ''.join(result)
    return result[p-1:t*m:m]