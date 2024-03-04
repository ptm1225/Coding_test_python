n = input()
left = n[0] if len(n) == 2 else '0'
right = n[-1]
first = left+right
count = 0

while first != left+right or count == 0:
    left, right = right, str(eval(left+'+'+right))[-1]
    count += 1

print(count)