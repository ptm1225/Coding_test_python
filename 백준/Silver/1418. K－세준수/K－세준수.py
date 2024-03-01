n = int(input())
k = int(input())

def is_prime(n):
    if n == 1:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

arr = [False] * (n+1)

for i in range(2, n+1):
    if is_prime(i) and i > k:
        for x in range(i, n+1, i):
            arr[x] = True

print(n-sum(arr))