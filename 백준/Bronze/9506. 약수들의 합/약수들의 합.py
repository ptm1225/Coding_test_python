while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            arr.append(i)
            arr.append(n//i)
    arr.sort()
    arr.pop()
    if int(n**0.5) == n**0.5:
        arr.pop()
    if sum(arr) == n:
        print(n, '=', ' + '.join(map(str, arr)))
    else:
        print(n, 'is NOT perfect.')