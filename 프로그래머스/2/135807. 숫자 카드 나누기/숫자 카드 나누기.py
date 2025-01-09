def gcd(a, b):
    while a % b != 0:
        a, b = b, a%b
    return b

def f(arrA, arrB):
    a = arrA[0]
    for b in arrA:
        a = gcd(a, b)
    
    return a if all(x%a != 0 for x in arrB) else 0

def solution(arrayA, arrayB):
    return max(f(arrayA, arrayB), f(arrayB, arrayA))