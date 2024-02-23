A, B = input().split()
arr = []
for i in range(len(B)-len(A)+1):
    s = (' ' * i) + A + ' ' * (len(B)-len(A)-i)
    count = 0
    for x, y in zip(s, B):
        if x == ' ':
            continue
        elif x != y:
            count += 1
    arr.append(count)

print(min(arr))