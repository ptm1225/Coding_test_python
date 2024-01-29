def solution(triangle):
    for i in range(1, len(triangle)):
        for x in range(len(triangle[i])):
            if x == 0:
                triangle[i][x] += triangle[i-1][x]
            elif x == (len(triangle[i]) - 1):
                triangle[i][x] += triangle[i-1][x-1]
            else:
                triangle[i][x] += max(triangle[i-1][x], triangle[i-1][x-1])
    
    return max(triangle[-1])