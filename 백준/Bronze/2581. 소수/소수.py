def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

arr = [False] + [True] * 10000
arr[1] = False
for i in range(2, 101):
    if is_prime(i):
        for x in range(2*i, 10001, i):
            arr[x] = False

n = int(input())
m = int(input())
ans = 0
mi = -1
for i in range(n, m+1):
    if arr[i]:
        if mi == -1:
            mi = i
        ans += i

if ans:
    print(ans)
    print(mi)
else:
    print(-1)