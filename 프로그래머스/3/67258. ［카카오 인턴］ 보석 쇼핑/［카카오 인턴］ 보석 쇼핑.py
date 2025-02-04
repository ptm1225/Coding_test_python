from collections import Counter

def solution(gems):
    c = Counter(gems)
    k = len(c)
    d = dict((x, 0) for x in c.keys())
    left, right = 0, 0
    d[gems[left]] += 1

    m = float('inf')
    cnt = 1
    result = [-1, -1]

    while right < len(gems):
        if cnt == k:
            if right - left < m:
                m = right - left
                result = [left+1, right+1]
            
            d[gems[left]] -= 1
            if d[gems[left]] == 0:
                cnt -= 1
            left += 1
        else:
            right += 1
            if right < len(gems):
                if d[gems[right]] == 0:
                    cnt += 1
                d[gems[right]] += 1
    
    return result