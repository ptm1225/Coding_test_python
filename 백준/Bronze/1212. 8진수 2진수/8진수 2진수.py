result = []
for i in input():
    a = bin(int(i))[2:]
    result.append('0'*(3-len(a)) + a)
print(int(''.join(result)))