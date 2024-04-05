import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
arr1 = set()
arr2 = set()
d = defaultdict(int)
for _ in range(n):
    arr1.add(input().rstrip())
for _ in range(m):
    s = input().rstrip()
    arr2.add(s)
    d[s] += 1
x = arr1 & arr2
result = 0
for i in x:
    result += d[i]
print(result)