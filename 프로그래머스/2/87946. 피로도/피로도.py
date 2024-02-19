from itertools import permutations

def func(k, arr):
    count = 0
    for i in arr:
        minimum, use = i[0], i[1]
        if minimum > k:
            return count
        else:
            k -= use
            count += 1
    return count

def solution(k, dungeons):
    return max([func(k, a) for a in permutations(dungeons, len(dungeons))])