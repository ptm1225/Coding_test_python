n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

while arr:
    i = arr[0]
    t = n-i+1 if i > (n//2 + 1) else -(i-1)
    answer += abs(t)
    for x in range(len(arr)):
        arr[x] += t
        
        if arr[x] > n:
            arr[x] -= n
        elif arr[x] < 1:
            arr[x] += n
            
    arr.pop(0)
    for x in range(len(arr)):
        arr[x] -= 1
    n -= 1
    
print(answer)