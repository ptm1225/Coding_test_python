import sys
input = sys.stdin.readline

S = input().rstrip()
bomb = list(input().rstrip())
n = len(bomb)
stack = []
i = 0
for x in S:
    stack.append(x)
    if stack[-n:] == bomb:
        for _ in range(n):
            stack.pop()
print(''.join(stack) if stack else 'FRULA')