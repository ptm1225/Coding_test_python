S = list(input())
l = S.count('1')
m = S.count('0')

for _ in range(l//2):
    S.pop(S.index('1'))

for _ in range(m//2):
    S.pop(len(S)-S[::-1].index('0')-1)

print(''.join(S))