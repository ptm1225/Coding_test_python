s = input()
d = {'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9}
result = 0
for i in s:
    for k, v in d.items():
        if i in k:
            result += 1+v
print(result)