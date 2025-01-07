def solution(mats, park):
    n = len(park)
    m = len(park[0])
    answer = -1
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                for num in mats:
                    if i+num <= n and j+num <= m and all(park[x][y] == "-1" for x in range(i, i+num) for y in range(j, j+num)):
                        answer = max(answer, num)
    return answer