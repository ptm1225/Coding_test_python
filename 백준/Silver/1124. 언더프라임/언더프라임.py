a, b = map(int, input().split())

prime_list = [False] + [True] * b
prime_list[1] = False

for i in range(2, int(b**0.5)+1):
    if prime_list[i]:
        for j in range(i*i, b+1, i):
            prime_list[j] = False

answer = 0
for n in range(a, b+1):
    count = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            n //= i
            count += 1
    if n != 1:
        count += 1
    
    if prime_list[count]:
        answer += 1
    
print(answer)