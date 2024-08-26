import sys
from itertools import combinations
from math import gcd
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    inp = list(map(int, input().split()))
    n, arr = inp[0], inp[1:]

    print(sum(gcd(a, b) for a, b in combinations(arr, 2)))