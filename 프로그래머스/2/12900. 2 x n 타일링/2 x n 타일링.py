def solution(n):
    if n < 3:
        return n
    else:
        a = [0] * (n+1)
        a[1] = 1
        a[2] = 2
        for i in range(3, n+1):
            a[i] = (a[i-1] + a[i-2]) % 1000000007
        return a[n]