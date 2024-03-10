inp = input()

tmp = ''
arr = []
for i in inp:
    if i.isdigit():
       tmp += i
    else:
        arr.append(str(int(tmp)))
        arr.append(i)
        tmp = ''
if tmp != '':
    arr.append(str(int(tmp)))
arr = ''.join(arr)
arr = arr.split('-')

result = eval(arr[0])
for i in range(1, len(arr)):
    result -= eval(arr[i])
print(result)