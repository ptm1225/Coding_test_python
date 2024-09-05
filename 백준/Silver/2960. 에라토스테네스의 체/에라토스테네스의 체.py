n, k = map(int, input().split())

prime = [0, 0] + [1] * (n-1)
cnt = 0
for i in range(2, n+1):
    if prime[i]:
        for x in range(i, n+1, i):
            if prime[x]:
                prime[x] = 0
                cnt += 1
                if cnt == k:
                    print(x)
                    exit()