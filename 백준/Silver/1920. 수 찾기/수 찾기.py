n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

end = len(a)-1
for num in b:
    s, e = 0, end
    while True:
        mid = (s+e)//2
        if s > e:
            if a[mid] == num:
                print(1)
            else:
                print(0)
            break
        if num < a[mid]:
            e = mid - 1
        else:
            s = mid + 1