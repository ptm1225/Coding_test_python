import sys
input = sys.stdin.readline

def bt(s, cnt):
    if cnt == N-1:
        t = ''
        for i, v in enumerate(s):
            t += str(i+1)
            t += v
        t += str(N)
        r = eval(''.join(t.split(' ')))
        if r == 0:
            print(t)
        return
    else:
        for x in ' +-':
            s.append(x)
            bt(s, cnt+1)
            s.pop()

T = int(input())
for _ in range(T):
    N = int(input())
    bt([], 0)
    print()