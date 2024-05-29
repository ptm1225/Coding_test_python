import sys
input = sys.stdin.readline

n = int(input())

prime = [False, False] + [True] * (n-1)
arr = []
for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for x in range(2*i, n+1, i):
            prime[x] = False

for i in range(2, n+1):
    if prime[i]:
        arr.append(i)
if arr:
    i, j = 0, 0
    t = 0
    cnt = 0
    
    while i <= j:
        if t < n:
            t += arr[j]
            if j < len(arr)-1:
                j += 1
        elif t > n:
            t -= arr[i]
            i += 1
        else:
            cnt += 1
            t -= arr[i]
            i += 1
    print(cnt)
else:
    print(0)