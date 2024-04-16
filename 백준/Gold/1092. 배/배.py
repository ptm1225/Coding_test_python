n = int(input())
c = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)
if max(box) > max(c):
    print(-1)
else:
    answer = 0
    while box:
        for i in range(len(c)):
            for j in range(len(box)):
                if c[i] >= box[j]:
                    del box[j]
                    break
        answer += 1
    print(answer)