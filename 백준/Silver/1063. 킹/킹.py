def func(king, step):
    tmp = king
    for s in step:
        if s == 'R':
            tmp = chr(ord(tmp[0]) + 1) + tmp[1]
        elif s == 'L':
            tmp = chr(ord(tmp[0]) - 1) + tmp[1]
        elif s == 'B':
            tmp = tmp[0] + str(int(tmp[1])-1)
        elif s == 'T':
            tmp = tmp[0] + str(int(tmp[1])+1)
    
    if ord('A') <= ord(tmp[0]) <= ord('H') and 1 <= int(tmp[1]) <= 8:
        return tmp
    return king
steps = []
king, stone, n = input().split()
for _ in range(int(n)):
    steps.append(input())

for step in steps:
    tmp_k, tmp_s = king, stone
    king = func(king, step)
    if king == stone:
        stone = func(stone, step)
        if king == stone:
            king, stone = tmp_k, tmp_s
    
print(king)
print(stone)