from collections import Counter
n = int(input())
card = Counter(input().split())
m = int(input())
arr = input().split()

for i in arr:
    if i in card.keys():
        print(card[i], end=' ')
    else:
        print(0, end=' ')