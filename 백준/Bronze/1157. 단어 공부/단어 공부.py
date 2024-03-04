from collections import Counter
arr = Counter(input().upper())
mx = max(arr.values())
print('?' if sum([mx == i for i in arr.values()]) > 1 else arr.most_common()[0][0])