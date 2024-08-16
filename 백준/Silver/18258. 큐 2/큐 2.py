from collections import deque
n = int(input())
queue = deque()
arr = []
for _ in range(n):
    arr.append(input().split())
for c in arr:
    if c[0] == 'push':
        queue.append(int(c[1]))
    elif c[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(queue))
    elif c[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif c[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)