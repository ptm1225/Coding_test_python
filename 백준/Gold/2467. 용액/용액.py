import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

i, j = 0, N-1
a, b = arr[i], arr[j]

while i < j:
    x = arr[i] + arr[j]
    if abs(x) < abs(a+b):
        a, b = arr[i], arr[j]
    
    if x > 0:
        j -= 1
    elif x < 0:
        i += 1
    else:
        break

print(a, b)