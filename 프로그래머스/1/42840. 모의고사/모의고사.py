def solution(answers):
    answer = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    idx = 0
    
    for x in answers:
        if one[idx % 5] == x:
            answer[0] += 1
        if two[idx % 8] == x:
            answer[1] += 1
        if three[idx % 10] == x:
            answer[2] += 1
        idx += 1
    m = max(answer)
    
    return [i+1 for i in range(3) if answer[i] == m]