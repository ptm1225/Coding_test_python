def func(string):
    result = []
    for s in string:
        arr = []
        n = len(s)
        while True:
            if n >= 4:
                arr.append('AAAA')
                n -= 4
            elif n >= 2:
                arr.append('BB')
                n -= 2
            else:
                if n != 0:
                    return -1
                else:
                    break
        result.append(''.join(arr))
    return result

inp = input()
string = inp.replace('.', ' ').split()
dot = inp.replace('X', ' ').split()

string = func(string)
if string == -1:
    print(-1)
else:
    if inp.startswith('.') and inp.endswith('.'):
        for i in range(len(string)):
            print(dot[i], end='')
            print(string[i], end='')
        print(dot[-1], end='')
    elif inp.startswith('.'):
        for i in range(len(string)):
            print(dot[i], end='')
            print(string[i], end='')
    elif inp.startswith('X') and inp.endswith('X'):
        for i in range(len(dot)):
            print(string[i], end='')
            print(dot[i], end='')
        print(string[-1], end='')
    else:
        for i in range(len(dot)):
            print(string[i], end='')
            print(dot[i], end='')