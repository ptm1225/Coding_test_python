d = [0] * 26
for i in input():
    d[ord(i)-97] += 1
print(*d)