ls = list(input())
rs = []
m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == 'L' and ls:
        rs.append(ls.pop())
    elif command[0] == 'D' and rs:
        ls.append(rs.pop())
    elif command[0] == 'B' and ls:
        ls.pop()
    elif command[0] == 'P':
        ls.append(command[1])
print(''.join(ls+rs[::-1]))