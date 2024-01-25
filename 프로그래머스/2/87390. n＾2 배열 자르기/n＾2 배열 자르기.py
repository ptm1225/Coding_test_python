def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        y = i//n
        x = i%n
        
        result = max(x, y) + 1
        answer.append(result)
    
    return answer