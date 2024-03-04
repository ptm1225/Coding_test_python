from collections import Counter
n = int(input())
arr = []
for _ in range(n):
    arr.append(input()[0])
a = Counter(arr)
print(''.join(sorted([i[0] for i in a.most_common() if i[1] >= 5])) if max(a.values()) >= 5 else 'PREDAJA')