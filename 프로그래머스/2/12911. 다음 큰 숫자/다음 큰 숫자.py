def solution(n):
    m = n
    while True:
        m += 1
        if bin(n)[2:].count('1') == bin(m)[2:].count('1'):
            break
    return m