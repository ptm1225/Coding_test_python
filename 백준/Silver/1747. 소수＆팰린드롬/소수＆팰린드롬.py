def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(input())
mx = 1000000
answer = 0
for i in range(n, mx+1):
    if str(i)[:] == str(i)[::-1] and is_prime(i):
        answer = i
        break

if not answer:
    i = mx
    while True:
        if str(i)[:] == str(i)[::-1] and is_prime(i):
            answer = i
            break
        i += 1

print(answer)