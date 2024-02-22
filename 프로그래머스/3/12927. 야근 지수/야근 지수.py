from collections import Counter

def solution(n, works):
    if sum(works) <= n:
        return 0
    else:
        d = Counter(works)
        for i in range(max(works), 0, -1):
            if n == 0:
                break

            if d[i] != 0:
                while d[i] and n:
                    d[i] -= 1
                    d[i-1] += 1
                    n -= 1
        return sum([v * k**2 for k,v in d.items()])