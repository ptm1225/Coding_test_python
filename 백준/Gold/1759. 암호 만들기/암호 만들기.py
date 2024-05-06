L, C = map(int, input().split())
arr = sorted(input().split())

def f(s):
    if len(s) == L:
        cnt = 0
        for x in 'aeiou':
            if x in s:
                cnt += 1
        if cnt >= 1 and L - cnt >= 2:
            print(''.join(s))
    else:
        for i in arr:
            if not s or s[-1] < i:
                s.append(i)
                f(s)
                s.pop()

f([])