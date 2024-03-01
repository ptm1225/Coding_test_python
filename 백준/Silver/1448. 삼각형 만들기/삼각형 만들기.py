n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
mx = -1
for i in range(n-2):
    a, b, c = arr[i], arr[i+1], arr[i+2]
    if a + b > c:
        mx = a+b+c
print(mx)