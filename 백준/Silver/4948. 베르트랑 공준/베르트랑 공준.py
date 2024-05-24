import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

z = 123456*2
arr = [False] + [True] * z
arr[1] = False
for i in range(2, int(z**0.5)+1):
    if is_prime(i):
        for x in range(2*i, 123456*2+1, i):
            arr[x] = False

while True:
    n = int(input().rstrip())
    if n == 0:
        break
    print(sum(arr[n+1:2*n+1]))