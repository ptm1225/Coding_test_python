n = int(input())
arr = list(map(int, input().split()))
stack = []
p = 1
while arr:
    if arr[0] == p:
        arr.pop(0)
        p += 1
    elif stack and stack[-1] == p:
        stack.pop()
        p += 1
    else:
        stack.append(arr.pop(0))

while stack:
    if stack[-1] == p:
        stack.pop()
        p += 1
    else:
        break

print('Nice' if p == n+1 else 'Sad')