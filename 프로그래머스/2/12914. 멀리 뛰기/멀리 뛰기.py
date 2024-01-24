def factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

def solution(n):
    count = 0
    for i in range(1, n+1):
        tmp = n-i
        count += factorial(i) // ((factorial(i-tmp)) * factorial(tmp))
    return count % 1234567