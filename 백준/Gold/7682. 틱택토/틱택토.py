import sys
input = sys.stdin.readline
while True:
    inp = input().rstrip()
    if inp == 'end':
        break

    x = inp.count('X')
    o = inp.count('O')
    d = [inp[:3], inp[3:6], inp[6:], inp[0]+inp[3]+inp[6], inp[1]+inp[4]+inp[7], inp[2]+inp[5]+inp[8], inp[0]+inp[4]+inp[8], inp[2]+inp[4]+inp[6]]
    if ('XXX' in d and 'OOO' not in d and x == o+1) or ('OOO' in d and 'XXX' not in d and x == o) or ('XXX' not in d and 'OOO' not in d and o == 4 and x == 5):
        print('valid')
    else:
        print('invalid')
