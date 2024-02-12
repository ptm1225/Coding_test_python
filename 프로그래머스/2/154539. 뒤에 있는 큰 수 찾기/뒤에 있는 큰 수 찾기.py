def solution(numbers):
    result = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers) - 1, -1, -1): # 뒤에서부터 검사
        
        while stack and numbers[i] >= stack[-1]: # 스택이 비지 않고 현재 검사중인 숫자가 스택의 위의 값보다 클 때
            stack.pop()
        
        if stack: # 스택에 값이 있다면 제일 위의 값은 현재 검사중인 숫자의 뒤 큰수
            result[i] = stack[-1]
        
        stack.append(numbers[i])
    
    return result