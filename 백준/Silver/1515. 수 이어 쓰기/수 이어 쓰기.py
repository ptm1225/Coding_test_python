num = input()
n = 0
idx = 0
while True:
    n += 1
    for s in str(n):
        if num[idx] == s:
            idx += 1
            if idx >= len(num):
                print(n)
                exit()