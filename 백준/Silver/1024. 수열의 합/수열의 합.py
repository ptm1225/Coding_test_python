N, L = map(int, input().split())

is_answer = False
for i in range(L, 101):
    n = N
    arr = []
    if i % 2 != 0 and n % i == 0:
        arr.append(n//i)
        for x in range(1, i//2 + 1):
            arr.append(n//i - x)
            arr.append(n//i + x)
    elif i % 2 == 0:
        for x in range(i//2):
            arr.append((n//(i//2))//2 - x)
            arr.append((n//(i//2))//2 + 1 + x)
    
    arr.sort()
    
    if arr and arr[0] >= 0 and list(range(arr[0], arr[-1]+1)) == arr and sum(arr) == N:
        is_answer = True
        break

if is_answer:
    for x in arr:
        print(x, end=' ')
else:
    print(-1)