import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
arr.sort()

def bt(n, cnt):
    if cnt == M:
        print(*n[1:])
        return

    for x in arr:
        if x > n[-1]:
            n.append(x)
            bt(n, cnt+1)
            n.pop()

bt([0], 0)