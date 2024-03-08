k = int(input())
stack = []
for _ in range(k):
    inp = int(input())
    if inp != 0:
        stack.append(inp)
    else:
        stack.pop()
print(sum(stack))