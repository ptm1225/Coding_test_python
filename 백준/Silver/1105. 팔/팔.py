l, r = input().split()

answer = 0

if len(l) == len(r):
    if l == r:
        answer = l.count('8')
    else:
        for i in range(len(l)):
            if l[i] == r[i]:
                if l[i] == '8':
                    answer += 1
                else:
                    continue
            else:
                break

print(answer)