def gcd(x, y):
    
    while y:
        x, y = y, x%y
    
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

def solution(arr):
    result = 1
    
    for i in arr:
        result = lcm(result, i)
    
    return result