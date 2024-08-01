def dfs(x, idx, cnt):
    if cnt == 6:
        print(*x)
        return

    for i in range(idx, k):
        x.append(S[i])
        dfs(x, i+1, cnt+1)
        x.pop()

while True:
    inp = input()
    if inp == '0':
        break
    A = list(map(int, inp.split()))
    k, S = A[0], A[1:]
    dfs([], 0, 0)
    print()