count = 0

def func(i, n, result, numbers, target):
    global count
    
    if i < n:
        func(i+1, n, result + numbers[i], numbers, target)
        func(i+1, n, result - numbers[i], numbers, target)
    
    elif i == n and result == target:
        count += 1

def solution(numbers, target):
    func(0, len(numbers), 0, numbers, target)
    return count