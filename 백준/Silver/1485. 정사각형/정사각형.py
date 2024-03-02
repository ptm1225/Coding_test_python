def dis(a, b):
    return abs((a[0]-b[0])**2 + (a[1]-b[1])**2)
t = int(input())
for _ in range(t):
    arr = []
    for _ in range(4):
        arr.append(list(map(int, input().split())))

    s = [dis(arr[0], arr[1]), dis(arr[0], arr[2]), dis(arr[0], arr[3]),
         dis(arr[1], arr[2]), dis(arr[1], arr[3]), dis(arr[2], arr[3])]

    if len(set(s)) == 2 and s.count(max(s)) == 2 and s.count(min(s)) == 4:
        print(1)
    else:
        print(0)