import sys
input = sys.stdin.readline

n = int(input())
arr = set()
for _ in range(n):
    v, op = input().rstrip().split()
    if op == 'enter':
        arr.add(v)
    elif op == 'leave':
        arr.remove(v)
for x in sorted(list(arr), reverse=True):
    print(x)