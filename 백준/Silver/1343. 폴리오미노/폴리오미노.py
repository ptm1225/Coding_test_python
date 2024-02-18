inp = input()

inp = inp.replace('XXXX', 'AAAA')
inp = inp.replace('XX', 'BB')

if 'X' in inp:
    print(-1)
else:
    print(inp)