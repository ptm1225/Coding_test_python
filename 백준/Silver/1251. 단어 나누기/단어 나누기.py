inp = input()

arr = []

for i in range(len(inp)-2):
    for j in range(i+1, len(inp)-1):
        one = list(reversed(inp[:i+1]))
        two = list(reversed(inp[i+1:j+1]))
        three = list(reversed(inp[j+1:]))
        arr.append(''.join(one+two+three))
arr.sort()
print(arr[0])