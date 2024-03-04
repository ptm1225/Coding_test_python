arr = []
for _ in range(8):
    arr.append(input())

result = 0
for i in arr[::2]:
    result += sum([x=='F' for x in i[::2]])
for i in arr[1::2]:
    result += sum([x=='F' for x in i[1::2]])

print(result)