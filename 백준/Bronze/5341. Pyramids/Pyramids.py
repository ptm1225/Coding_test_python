def f(n):
    return n+f(n-1) if n > 1 else 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(f(n))