n = int(input())
arr = []
for _ in range(n):
    s = input()
    for a in arr:
        if s in a:
            break
    else:
        arr.append([s[i:] + s[:i] for i in range(len(s))])

print(len(arr))