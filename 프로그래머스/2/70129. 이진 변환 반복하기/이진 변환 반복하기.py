def solution(s):
    count = 0
    result = 0
    while True:
        count += 1
        result += len([i for i in s if i == '0'])
        n = len([i for i in s if i != '0'])
        if n == 1:
            break
        s = str(bin(n))[2:]
    return [count, result]