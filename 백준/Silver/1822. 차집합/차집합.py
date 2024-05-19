na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

arr = list(a.difference(b))
l = len(arr)
print(l)
if l:
    print(*sorted(arr))