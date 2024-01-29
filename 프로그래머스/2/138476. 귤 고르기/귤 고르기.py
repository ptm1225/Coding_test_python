def solution(k, tangerine):
    d = dict()
    result = 0
    SUM = 0
    
    for v in tangerine:
        if v not in d.keys():
            d[v] = 1
        else:
            d[v] += 1
    
    for v in sorted(d.values(), reverse=True):
        if k < v:
            result = 1
            break
        elif k <= SUM:
            continue
        else:
            SUM += v
            result += 1
    return result