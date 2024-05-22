import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().rstrip().split())
    if n == m == 0:
        break
    a = set()
    b = set()
    for _ in range(n):
        a.add(int(input().rstrip()))
    for _ in range(m):
        b.add(int(input().rstrip()))
    print(len(a&b))