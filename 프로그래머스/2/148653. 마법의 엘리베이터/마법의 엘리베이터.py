from collections import deque
def solution(storey):
    q = deque()
    storey = str(storey)[::-1]
    n = len(storey)
    q.append((0, 0, 0))
    result = 2 ** 10
    while q:
        i, total, c = q.popleft()
        a = int(storey[i]) + c
        if i == n-1:
            result = min(result, total+a, total+(10-a)+1)
        else:
            if a >= 10:
                q.append((i+1, total, 1))
            else:
                q.append((i+1, total+a, 0))
                q.append((i+1, total+(10-a), 1))
        
    return result