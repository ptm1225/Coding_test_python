n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
result = 5
for i in arr:
    for x in range(-4, 5):
        a = 5 - sum(arr.count(i+x+z) for z in range(5))
        result = min(result, a)
print(result)