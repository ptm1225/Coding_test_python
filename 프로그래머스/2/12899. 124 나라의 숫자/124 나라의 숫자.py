from math import ceil
def solution(n):
    t = 3
    a = ['4','1','2']
    result = ''
    while n > 0:
        if t == 3:
            result += a[n%3]
        else:
            result += a[ceil(n/(t//3))%3]
        n -= t
        t *= 3
        
    return result[::-1]