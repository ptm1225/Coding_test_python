import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
stack = deque()
arr = []
for _ in range(n):
    arr.append(input().rstrip().split())
for x in arr:
    if x[0] == '1':
        stack.append(x[1])
    elif x[0] == '2':
        print(stack.pop() if stack else -1)
    elif x[0] == '3':
        print(len(stack))
    elif x[0] == '4':
        print(0 if stack else 1)
    elif x[0] == '5':
        print(stack[-1] if stack else -1)