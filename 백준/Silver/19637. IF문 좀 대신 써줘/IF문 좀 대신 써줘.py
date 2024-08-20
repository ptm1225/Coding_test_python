import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().rstrip().split()) for _ in range(n)]

for _ in range(m):
    x = int(input().rstrip())
    i, j = 0, n-1
    while i <= j:
        mid = (i+j)//2
        t = int(arr[mid][1])
        
        if x > t:
            i = mid+1
        else:
            j = mid-1
    print(arr[i][0])