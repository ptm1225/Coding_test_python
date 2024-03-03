n = int(input())
post = list(input())
arr = [input() for _ in range(n)]
func = ['+', '-', '*', '/']
for i in range(n):
    word = chr(65+i)
    for x in range(len(post)):
        if post[x] == word:
            post[x] = arr[i]

stack = []
for i in post:
    if i not in func:
        stack.append(i)
    else:
        s = stack.pop()
        f = stack.pop()
        stack.append(str(eval(f+i+s)))

print('{0:.2f}'.format(float(stack[0])))