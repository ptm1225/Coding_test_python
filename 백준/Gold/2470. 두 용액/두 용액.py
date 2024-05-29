import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
i, j = 0, n-1
left, right = arr[i], arr[j]

while i < j:
    t = arr[i] + arr[j]
    if abs(t) < abs(left+right):
        left, right = arr[i], arr[j]
    if t < 0:
        i += 1
    elif t > 0:
        j -= 1
    else:
        ans = t
        break
    
print(left, right)