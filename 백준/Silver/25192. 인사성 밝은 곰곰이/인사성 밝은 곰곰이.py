cnt = 0
s = set()
for _ in range(int(input())):
    x = input()
    if x == 'ENTER':
        s = set()
    else:
        if x not in s:
            cnt += 1
            s.add(x)
print(cnt)