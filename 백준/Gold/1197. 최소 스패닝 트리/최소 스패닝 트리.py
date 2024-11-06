V, E = map(int, input().split())

s = list(range(V+1))
edges = sorted([tuple(map(int, input().split())) for _ in range(E)], key=lambda x:x[2])
total = 0

def f(x):
    if x == s[x]:
        return x
    return s[x]

for a,b,c in edges:
    fa, fb = f(a), f(b)
    if fa != fb:
        if fa < fb:
            pass
        else:
            fa, fb = fb, fa
        for i, v in enumerate(s):
            if v == fb:
                s[i] = fa
        total += c
print(total)