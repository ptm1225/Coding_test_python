import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    inp = input().rstrip()
    if inp == '':
        break
    x = int(inp) * 10**7
    n = int(input())
    L = []
    for _ in range(n):
        L.append(int(input()))
    L.sort()
    
    l, r = 0, n-1
    while l < r:
        z = L[l] + L[r]
        if z < x:
            l += 1
        elif z > x:
            r -= 1
        else:
            print('yes', L[l], L[r])
            break
    else:
        print('danger')