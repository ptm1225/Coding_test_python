from collections import deque

def solution(priorities, location):
    di, dv = location, priorities[location]
    
    iq = deque([i for i in range(len(priorities))])
    vq = deque(priorities)
    
    count = 1
    
    while vq:
        i = iq.popleft()
        v = vq.popleft()
        
        if not vq and i == di and v == dv:
            return count
        
        if v < max(vq):
            vq.append(v)
            iq.append(i)
        else:
            if i == di and v == dv:
                return count
            else:
                count += 1