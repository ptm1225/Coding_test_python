n = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x*0.5)+1):
        if x%i==0:
            return False
    return True

def f(num, cnt):
    if cnt == n:
        print(num)
    else:
        for i in range(10):
            if cnt == 0 and i == 0:
                continue
            num = num*10 + i
            if is_prime(num):
                f(num, cnt+1)
            num = num // 10

f(0, 0)