import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def bt(n, cnt):
    if cnt == M:
        print(*n)
        return

    for x in arr:
        n.append(x)
        bt(n, cnt+1)
        n.pop()

bt([], 0)