import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = 100
b = 100
for _ in range(n):
    x, y = map(int, input().split())
    if x < y:
        a -= y
    elif x > y:
        b -= x
print(a)
print(b)