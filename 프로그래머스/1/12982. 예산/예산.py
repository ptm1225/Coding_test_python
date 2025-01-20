def solution(d, budget):
    total = 0
    answer = 0
    for x in sorted(d):
        if total >= budget:
            break
        total += x
        answer += 1
    if total > budget:
        answer -= 1
    return answer