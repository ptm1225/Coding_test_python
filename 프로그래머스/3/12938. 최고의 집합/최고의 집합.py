def solution(n, s):
    if n > s:
        return [-1]
    else:
        arr = [s//n]*n
        z = s%n
        i = -1
        while z:
            arr[i] += 1
            i-=1
            z-=1
        return arr