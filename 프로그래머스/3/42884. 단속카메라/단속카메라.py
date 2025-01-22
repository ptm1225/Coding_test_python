def solution(routes):
    routes.sort(key=lambda x:x[1])
    c = -30001
    count = 0
    
    for a, b in routes:
        if c < a:
            count += 1
            c = b
    
    return count