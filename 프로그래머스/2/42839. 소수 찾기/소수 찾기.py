from itertools import combinations, permutations

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    count = 0
    arr = []
    for i in range(1, len(numbers)+1):
        for k in permutations(numbers, i):
            t = int(''.join(k))
            if is_prime(t) and t not in arr:
                print(t)
                arr.append(t)
                count += 1
    return count