def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max([v for idx, v in enumerate(land[i-1]) if idx != j])
    
    return max(land[-1])