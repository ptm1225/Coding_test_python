def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def bt(t, cnt):
    if cnt == 4:
        if sum(t) == n:
            print(*t)
            exit(0)
    else:
        for i, x in enumerate(prime):
            if x:
                t.append(i)
                bt(t, cnt+1)
                t.pop()

n = int(input())

prime = [True] * (n+1)
prime[0] = False
prime[1] = False

for i in range(2, int(n**0.5)+2):
    if is_prime(i):
        for x in range(2*i, n+1, i):
            prime[x] = False

t = []
cnt = 0

if n > 20:
    if n % 2 != 0:
        t.append(2)
        cnt += 1
    prime[2] = False
bt(t, cnt)
print(-1)