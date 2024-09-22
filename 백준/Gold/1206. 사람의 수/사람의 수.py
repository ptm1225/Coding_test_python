n = int(input())
arr = [int(input().split('.')[1]) for _ in range(n)]

cnt = 1
while True:
    for i in arr:
        num = i * cnt
        if num % 1000 != 0:
            num = num - (num % 1000) + 1000
        num = int(num / cnt)
        if num != i:
            cnt += 1
            break
    else:
        print(cnt)
        break