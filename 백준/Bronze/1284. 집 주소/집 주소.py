while True:
    inp = input()
    if inp == '0':
        break
    count = 1
    for i in inp:
        if i == '1':
            count += 2
        elif i == '0':
            count += 4
        else:
            count += 3
        count += 1
    print(count)