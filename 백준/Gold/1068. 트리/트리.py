n = int(input())
arr = list(map(int, input().split()))
d = int(input())
cnt = 0

def f(n):
    for i, v in enumerate(arr):
        if v == n:
            arr[i] = -2
            f(i)

f(d)
arr[d] = -2
for i in range(n):
    if arr[i] != -2 and arr.count(i) == 0:
        cnt += 1
print(cnt)