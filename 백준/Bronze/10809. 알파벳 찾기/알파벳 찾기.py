z = [-1 for _ in range(26)]
for i, v in enumerate(input()):
    if z[ord(v)-97] == -1:
        z[ord(v)-97] = i
for i in z:
    print(i, end=' ')