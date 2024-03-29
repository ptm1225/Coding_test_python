import sys
input = sys.stdin.readline

n = int(input().rstrip())
elements = list(map(int, input().rstrip().split()))
stack = []
result = [-1] * n
for i, e in enumerate(elements):
    while stack and stack[-1][1] < e:
        idx, v = stack.pop()
        result[idx] = e
    
    stack.append((i, e))

print(*result)