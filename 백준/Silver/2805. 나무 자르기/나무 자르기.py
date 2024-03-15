n, m = map(int, input().split())
tree = list(map(int, input().split()))
s = sum(tree)

left = 0
right = max(tree)

while left <= right:
    mid = (left+right)//2
    d = sum([i-mid for i in tree if i > mid])
    if d < m:
        right = mid - 1
    else:
        left = mid + 1

print(right)