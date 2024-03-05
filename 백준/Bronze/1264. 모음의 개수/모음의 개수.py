while True:
    inp = input().lower()
    if inp == '#':
        break
    count = 0
    for i in inp:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    print(count)