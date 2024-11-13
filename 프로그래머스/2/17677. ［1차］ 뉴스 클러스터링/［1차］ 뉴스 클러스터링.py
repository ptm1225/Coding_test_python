import re
from collections import Counter

def create_multiset(s):
    s = s.lower()
    return [s[i:i+2] for i in range(len(s) - 1) if re.match("[a-z]{2}", s[i:i+2])]

def jaccard_similarity(str1, str2):
    multiset1 = create_multiset(str1)
    multiset2 = create_multiset(str2)

    counter1 = Counter(multiset1)
    counter2 = Counter(multiset2)

    intersection = counter1 & counter2
    union = counter1 | counter2

    intersection_size = sum(intersection.values())
    union_size = sum(union.values())

    if union_size == 0:
        return 65536

    jaccard_index = intersection_size / union_size
    return int(jaccard_index * 65536)

def solution(str1, str2):
    return jaccard_similarity(str1, str2)
    