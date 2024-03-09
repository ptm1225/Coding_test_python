n = int(input())
if n == 0:
    print(0)
else:
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    
    s = int(n*0.15) if (n*0.15)%1 < 0.5 else int(n*0.15)+1
    a = arr[s:n-s]
    result = int(sum(a)/len(a)) if sum(a)/len(a)%1 < 0.5 else int(sum(a)/len(a))+1
    print(result)