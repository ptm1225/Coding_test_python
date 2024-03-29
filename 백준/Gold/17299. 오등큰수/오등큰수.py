from collections import Counter
import sys
input = sys.stdin.readline

n = int(input().rstrip())
elements = list(map(int, input().rstrip().split()))
d = Counter(elements)
stack = []
result = [-1] * n
for i, e in enumerate(elements):
    c = d[e]
    while stack and stack[-1][1] < c:
        idx, v = stack.pop()
        result[idx] = e
    
    stack.append((i, d[e]))

print(*result)