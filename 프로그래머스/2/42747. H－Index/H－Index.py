def solution(citations):
    arr = []
    for i in range(max(citations)):
        over = [j >= i for j in citations].count(True)
        if over >= i:
            arr.append(i)
    
    if len(arr) == 0:
        return min(citations)
    else:
        return max(arr)