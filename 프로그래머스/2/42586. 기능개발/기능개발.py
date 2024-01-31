from math import ceil

def solution(progresses, speeds):
    result = []
    count = 0
    days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    print("first days :", days)
    while True:
        if count == 0:
            days = [day - 1 for day in days]
        
        tmp = len(days)
        
        for i in range(len(days)):
            if i == 0 and days[i] <= 0:
                days.pop(0)
                count += 1
                break
        
        if len(days) == tmp and count > 0:
            result.append(count)
            count = 0
            if len(days) == 0:
                break
        else:
            pass
    return result