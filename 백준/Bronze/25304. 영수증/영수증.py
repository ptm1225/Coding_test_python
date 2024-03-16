total = int(input())
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    total -= a*b
if total:
    print('No')
else:
    print('Yes')