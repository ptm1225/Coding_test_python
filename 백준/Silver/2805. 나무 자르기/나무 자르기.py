import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))

i, j = 0, max(height)

while i <= j:
    mid = (i+j)//2
    s = sum([h-mid for h in height if h-mid > 0])
    
    if s < m:
        j = mid - 1
    else:
        i = mid + 1
print(j)