n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

result = []
for i in zip(*arr):
    if len(set(i)) == 1:
        result.append(i[0])
    else:
        result.append('?')
print(''.join(result))