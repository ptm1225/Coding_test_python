n, m, b = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

mn = min(min(i) for i in arr)
mx = max(max(i) for i in arr)

result = []
for x in range(mn, mx+1):
    under = 0
    over = 0
    inven = b
    for i in range(n):
        for j in range(m):
            s = arr[i][j] - x
            if s > 0:
                over += s
                inven += s
            elif s < 0:
                under -= s
    if inven >= under:
        result.append((over*2 + under, x))

r = min([i[0] for i in result])
result.sort(key=lambda x:x[1], reverse=True)

for i in result:
    if i[0] == r:
        print(*i)
        break