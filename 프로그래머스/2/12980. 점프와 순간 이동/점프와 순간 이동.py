def solution(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
            continue
        else:
            n -= 1
            count += 1
    return count