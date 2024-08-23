n, k = map(int, input().split())

def f(s):
    z = sum(s)
    if z > n:
        return
    elif z == n:
        global k
        k -= 1
        if k == 0:
            print('+'.join(map(str, s)))
            exit()
        return

    for x in [1, 2, 3]:
        s.append(x)
        f(s)
        s.pop()

f([])
print(-1)