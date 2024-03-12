import sys

m = int(sys.stdin.readline())
S = set()
for _ in range(m):
    i = sys.stdin.readline().split()
    if i[0] == 'add':
        S.add(int(i[1]))
    elif i[0] == 'remove':
        if int(i[1]) in S:
            S.remove(int(i[1]))
    elif i[0] == 'check':
        if int(i[1]) in S:
            print(1)
        else:
            print(0)
    elif i[0] == 'toggle':
        if int(i[1]) in S:
            S.remove(int(i[1]))
        else:
            S.add(int(i[1]))
    elif i[0] == 'all':
        S = set(range(1,21))
    elif i[0] == 'empty':
        S = set()