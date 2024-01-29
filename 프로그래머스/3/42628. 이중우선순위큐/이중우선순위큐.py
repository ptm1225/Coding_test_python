def solution(operations):
    arr = []
    for i, v in enumerate(operations):
        if operations[i].startswith("I"):
            arr.append(int(v[2:]))
            arr.sort()
            print(arr)
        else:
            if len(arr) == 0:
                continue
                
            if operations[i] == "D 1":
                arr.pop()
            elif operations[i] == "D -1":
                arr = arr[1:]
    
    if len(arr) == 0:
        return [0, 0]
    else:
        return [max(arr), min(arr)]