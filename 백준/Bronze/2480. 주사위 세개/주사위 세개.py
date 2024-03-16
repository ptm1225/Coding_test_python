from collections import Counter
d=Counter(list(map(int, input().split())))
k,v = d.most_common()[0]
if v == 3:
    print(10000 + k*1000)
elif v == 2:
    print(1000 + k*100)
else:
    print(max(d.keys())*100)