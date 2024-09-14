total = 0
result = 0
for _ in range(10):
    u, d = map(int, input().split())
    total -= u
    total += d
    result = max(result, total)
print(result)