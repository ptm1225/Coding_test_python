result = []
n = int(input())
while n:
    name = []
    for _ in range(n):
        name.append(input())

    arr = []
    while True:
        event = input().split()
        if len(event) == 1:
            n = int(event[0])
            break
        if event[0] not in arr:
            arr.append(event[0])
        else:
            arr.remove(event[0])
    result.append(name[int(arr[0])-1])

for i, v in enumerate(result):
    print(i+1, v)