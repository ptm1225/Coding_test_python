def solution(s):
    stack = [0]
    for i in s:
        if stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    return 1 if stack == [0] else 0