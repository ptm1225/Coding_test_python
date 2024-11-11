def solution(diffs, times, limit):
    answer = 0
    n = len(diffs)
    left, right = 1, 100000
    while left < right:
        level = (left + right) // 2
        total = 0
        for i in range(n):
            if diffs[i] <= level:
                total += times[i]
            else:
                total += (times[i] + times[i-1])*(diffs[i] - level) + times[i]
        if total > limit:
            left = level + 1
        elif total < limit:
            right = level
        else:
            return level
    
    return left