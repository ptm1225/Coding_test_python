start, end = map(int, input().split())

arr = [True] * (end - start + 1)

for i in range(2, int(end**0.5)+1):
    t = i**2
    s = (start//t + 1) if start % t != 0 else start//t
    for j in range(s * t, end + 1, t):
        arr[j-start] = False

print(sum(arr))