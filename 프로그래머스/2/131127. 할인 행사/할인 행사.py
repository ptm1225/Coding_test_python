import copy

def solution(want, number, discount):
    count = 0
    n = sum(number)
    
    for x in range(len(discount)):
        tmp_number = copy.deepcopy(number)
        
        limit = len(discount) - x if len(discount) - x < n else n
        for i in range(x, limit + x):
            if discount[i] in want and tmp_number[want.index(discount[i])] > 0:
                tmp_number[want.index(discount[i])] -= 1
                
                if all([n == 0 for n in tmp_number]):
                    count += 1
                    break
        
    return count