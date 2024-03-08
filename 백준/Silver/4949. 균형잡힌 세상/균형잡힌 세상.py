while True:
    inp = input()
    if inp == '.':
        break
    stack = []
    for i in inp:
        if i == '(' or i == '[':
            stack.append(i)
        elif i ==')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
    if stack:
        print('no')
    else:
        print('yes')