n = int(input())
arr = [int(input()) for _ in range(n)]

s = [0] * 1000001
for v in arr:
    s[v] += 1

for v in arr:
    if v > 1:
        cnt = 0
        for x in range(1, int(v**0.5)+1):
            if v%x == 0:
                cnt += s[x]
                cnt += s[v//x]
                if v**0.5 == v//x:
                    cnt -= s[v//x]
        print(cnt-1)
    else:
        print(s[1]-1)