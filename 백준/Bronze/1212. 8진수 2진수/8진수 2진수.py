is_first = True
for i in input():
    a = bin(int(i))[2:]
    if is_first:
        is_first = False
        print(a, end='')
    else:
        print('0'*(3-len(a)) + a, end='')