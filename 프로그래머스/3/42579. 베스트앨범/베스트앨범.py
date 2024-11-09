from collections import defaultdict
def solution(genres, plays):
    d = defaultdict(list)
    total = defaultdict(int)
    for i in range(len(genres)):
        d[genres[i]].append((i, plays[i]))
        total[genres[i]] +=  plays[i]
    result = []
    
    total = sorted(total.items(), key=lambda x:x[1], reverse=True)
    
    for gen in total:
        s = sorted(d[gen[0]], key=lambda x:x[1], reverse=True)
        result.append(s[0][0])
        if len(s) > 1:
            result.append(s[1][0])
    
    return result
