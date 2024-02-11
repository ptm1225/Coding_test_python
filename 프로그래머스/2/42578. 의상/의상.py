def solution(clothes):
    d = {}
    count = 1
    
    for cloth in clothes:
        kind, name = cloth[1], cloth[0]
        if kind not in d.keys():
            d[kind] = 1
        else:
            d[kind] += 1
    
    for k, v in d.items():
        count *= v+1
    
    return count - 1