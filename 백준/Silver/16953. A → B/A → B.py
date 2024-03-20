from collections import deque
a, b = map(int, input().split())

q = deque()
q.append((a, 1))
result = -1
while q:
    v, cnt = q.popleft()
    if v == b:
        result = cnt
        break

    one = 2*v
    two = int(str(v)+'1')
    if one <= b:
        q.append((one, cnt+1))
    if two <= b:
        q.append((two, cnt+1))
print(result)