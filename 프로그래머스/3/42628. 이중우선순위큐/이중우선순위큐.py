def solution(operations):
    arr = []
    for i, v in enumerate(operations):
        op, num = operations[i].split(' ')
        if op == "I":
            arr.append(int(v[2:]))
            arr.sort()
        elif op == "D":
            if len(arr) == 0:
                continue
                
            if num == "1":
                arr.pop()
            elif num == "-1":
                arr = arr[1:]
    
    if len(arr) == 0:
        return [0, 0]
    else:
        return [max(arr), min(arr)]