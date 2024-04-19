s = input()
cnt = 0
while len(s) > 1:
    s = str(sum(int(i) for i in list(s)))
    cnt += 1
print(cnt)
print('YES' if int(s) % 3 == 0 else 'NO')