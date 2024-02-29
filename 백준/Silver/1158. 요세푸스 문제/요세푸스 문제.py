n, k = map(int, input().split())
arr = list(range(1, n+1))
p = 0
result = []
while arr:
    p = (p+k-1) % len(arr)
    result.append(str(arr.pop(p)))
print('<'+', '.join(result)+'>')