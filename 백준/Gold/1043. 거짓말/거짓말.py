n, m = map(int, input().split())
t = input().split()

if t == '0':
    pass
else:
    l, li = int(t[0]), list(map(int, t[1:]))

num = [0] * (n+1)
for x in li:
    num[x] = 1

arr = [list(map(int, input().split()))[1:] for _ in range(m)]
visited = [0] * m

while li:
    x = li.pop(0)
    for i, y in enumerate(arr):
        if not visited[i] and x in y:
            visited[i] = 1
            for k in y:
                if not num[k]:
                    num[k] = 1
                    li.append(k)
print(m - sum(visited))