def solution(n):
    a = [0, 1]
    i = 2
    while i < n+1:
        a.append(a[i-1] + a[i-2])
        i += 1
    return a[-1] % 1234567