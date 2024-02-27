a, b = map(int, input().split())

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

answer = 0
prime_list = [i for i in range(b+1) if is_prime(i)]

for n in range(a, b+1):
    if n in prime_list:
        continue
    
    else:
        arr = []
        i = 0
        while n != 1:
            if n % prime_list[i] == 0:
                arr.append(prime_list[i])
                n //= prime_list[i]
                i = 0
            else:
                i += 1
        
        if is_prime(len(arr)):
            answer += 1

print(answer)