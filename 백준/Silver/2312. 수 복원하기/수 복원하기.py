from collections import defaultdict
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

prime = []
for i in range(2, 100000):
    if is_prime(i):
        prime.append(i)

t = int(input())
for _ in range(t):
    n = int(input())
    z = defaultdict(int)
    while n > 1:
        for p in prime:
            if n%p == 0:
                z[p] += 1
                n //= p
                break
    for k, v in z.items():
        print(k, v)