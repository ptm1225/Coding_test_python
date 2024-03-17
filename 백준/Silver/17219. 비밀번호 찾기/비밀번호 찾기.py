import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
d = defaultdict()
for _ in range(n):
    url, pwd = input().rstrip().split()
    d[url] = pwd

for _ in range(m):
    print(d[input().rstrip()])