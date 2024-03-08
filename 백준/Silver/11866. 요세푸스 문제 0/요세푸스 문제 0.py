n, k = map(int, input().split())
q = list(range(1, n+1))
result = []
i = 0
while q:
    i = (i+k-1)%len(q)
    result.append(str(q.pop(i)))

print('<'+', '.join(result)+'>')