def solution(numbers):
    result = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3,reverse=True)
    
    for x in numbers:
        result = result + x
    
    return str(int(result))