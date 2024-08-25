A, B = map(int, input().split())
m = int(input())
arr = reversed(list(map(int, input().split())))

t = 0
for i, v in enumerate(arr):
    t += v * (A ** i)

result = []

while t >= B:
    result.append(t%B)
    t //= B
if t > 0:
    result.append(t)

print(*reversed(result))