k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

s = 1
e = max(arr)

while s <= e:
    mid = (s+e)//2
    if sum([i//mid for i in arr]) >= n:
        s = mid + 1
    else:
        e = mid - 1

print(e)