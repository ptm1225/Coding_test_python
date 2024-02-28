from itertools import combinations as c
n, m, k = map(int, input().split())
a = range(1, n+1)
count = 0
total = 0
for i in c(a, m):
    for j in c(a, m):
        if len(set(i) & set(j)) >= k:
            count += 1
        
        total += 1

print(count/total)