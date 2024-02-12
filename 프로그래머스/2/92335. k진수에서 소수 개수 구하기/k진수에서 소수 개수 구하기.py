def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    
    arr = []
    count = 0
    
    while n:
        arr.append(n % k)
        n = n // k
    
    s = list(map(int, ''.join(map(str, reversed(arr))).replace('0', ' ').split()))
    
    for i in s:
        if is_prime(i):
            count += 1
    
    return count