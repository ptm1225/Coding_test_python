import sys
input = sys.stdin.readline

n = input().rstrip()
r = len(n)-1
arr = [0] * 10

if r == 0:
    for i in range(1, int(n)+1):
        arr[i] += 1
    print(*arr)
else:
    for i, v in enumerate(n):
        v = int(v)
        if i == 0:
            arr[v] += int(n[i+1:])+1
            for idx in range(v-1, 0, -1):
                arr[idx] += 10**(r-i)
        elif i == r:
            for idx in range(10):
                arr[idx] += int(n[:i])
            arr[0] -= 1
            for idx in range(v+1):
                arr[idx] += 1
        else:
            arr[v] += int(n[i+1:])+1
            for idx in range(v-1, -1, -1):
                arr[idx] += 10**(r-i)
            for idx in range(10):
                arr[idx] += int(n[:i]) * 10**(r-i)
            arr[0] -= 10**(r-i)
        
    print(*arr)