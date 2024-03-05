n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

a = 0
b = 0
for i in range(n):
    if 'X' not in arr[i]:
        a += 1
for j in range(m):
    is_b = True
    for i in range(n):
        if arr[i][j] == 'X':
            is_b = False
            break
    if is_b:
        b += 1

print(max(a, b))